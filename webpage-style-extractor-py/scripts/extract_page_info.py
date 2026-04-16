#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
页面信息提取脚本（统一完整版）

功能目标：
1. 提取页面基础设计信息：颜色、排版、组件、布局、CSS变量。
2. 提取交互设计信息：hover / active / focus / animation / transition。
3. 执行真实交互采样：悬停与点击（按下态、点击后态）样式变化。
4. 输出结构化 JSON、页面截图与提取摘要，便于高保真页面风格复刻。

使用方式：
    python extract_page_info.py --url <URL> --output_dir <输出目录>
"""

import asyncio
import argparse
import json
import re
from datetime import datetime
from pathlib import Path

from playwright.async_api import async_playwright


class PageExtractor:
    """
    页面提取器主类。

    设计说明：
    - 所有采集结果集中写入 self.data，最终统一落盘，避免多处文件写入导致结构不一致。
    - 先做静态样式提取，再做交互模拟采样，确保基础数据与交互数据都完整可用。
    """

    def __init__(self, url: str, output_dir: str):
        self.url = url
        self.output_dir = Path(output_dir)

        # 统一输出结构：产品型 SKILL 可直接消费该 JSON。
        self.data = {
            "url": url,
            "timestamp": datetime.now().isoformat(),
            "colors": {
                "primary": None,
                "secondary": None,
                "accent": None,
                "text": [],
                "background": [],
                "border": [],
                "gradients": [],
                "frequency": {},
            },
            "typography": {
                "fonts": [],
                "sizes": [],
                "weights": [],
                "lineHeights": [],
                "fontFamilies": [],
            },
            "components": {
                "buttons": [],
                "cards": [],
                "inputs": [],
                "navs": [],
                "links": [],
                "modals": [],
            },
            "layout": {
                "containers": [],
                "grids": [],
                "spacing": [],
                "viewport": {},
            },
            "cssVariables": {},
            "interactions": {
                "hoverEffects": [],
                "clickEffects": [],
                "focusEffects": [],
                "animations": [],
                "transitions": [],
                "simulatedHoverEffects": [],
                "simulatedClickEffects": [],
                "simulatedInteractions": [],
            },
            "interactiveElements": [],
            "designTokens": {},
            "industry": None,
            "screenshot": None,
        }

    @staticmethod
    def rgb_to_hex(rgb):
        """将 `rgb/rgba` 颜色统一转为 `#RRGGBB`，便于后续去重与统计。"""
        if not rgb or rgb in ("transparent", "rgba(0, 0, 0, 0)"):
            return None
        match = re.match(r"rgba?\((\d+),\s*(\d+),\s*(\d+)", rgb)
        if not match:
            return rgb
        r, g, b = int(match.group(1)), int(match.group(2)), int(match.group(3))
        return f"#{(1 << 24) + (r << 16) + (g << 8) + b:06X}"

    async def extract(self):
        """
        提取流程总入口。

        执行顺序：
        1) 打开页面并等待动态内容稳定；
        2) 采集静态样式；
        3) 采集交互规则；
        4) 执行真实交互采样；
        5) 输出 JSON / 截图 / 摘要。
        """
        async with async_playwright() as p:
            # set headless to False to debug page loading
            # browser = await p.chromium.launch(headless=True)
            browser = await p.chromium.launch(
                headless=True,  # 对于复杂站点，建议使用有头模式，更不易被检测
                args=[
                    '--disable-blink-features=AutomationControlled',  # 关键：移除自动化控制标记[reference:0]
                    '--no-sandbox',
                    '--disable-infobars'  # 禁用“Chrome 正受到自动化软件控制”的信息栏[reference:1]
                ]
            )
            # 2. 在 context 阶段模拟真实用户的设备和网络环境
            context = await browser.new_context(
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',  # 使用真实、常见的 UA[reference:2]
                viewport={'width': 1920, 'height': 1080},  # 常见分辨率[reference:3]
                locale='zh-CN',  # 设置与IP一致的语言环境
                timezone_id='Asia/Shanghai'  # 设置时区
            )
            # page = await browser.new_page()
            page = await context.new_page()

            # 3. 在页面加载前注入脚本，覆盖 JavaScript 环境中的自动化属性
            await page.add_init_script("""
                // 覆盖 webdriver 属性
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined
                });
                // 覆盖 Chrome 的运行时属性
                window.chrome = {
                    runtime: {}
                };
                // 覆盖权限查询，避免暴露 headless 特征
                const originalQuery = window.navigator.permissions.query;
                window.navigator.permissions.query = (parameters) => (
                    parameters.name === 'notifications' ?
                        Promise.resolve({ state: Notification.permission }) :
                        originalQuery(parameters)
                );
            """)  # [reference:4][reference:5]

            try:
                print(f"\n🌐 正在访问: {self.url}\n")
                await page.goto(self.url, wait_until="domcontentloaded", timeout=60000)
                print("⏳ 等待动态内容加载...")
                await page.wait_for_timeout(5000)

                # ---------- 基础视觉信息 ----------
                await self.extract_css_variables(page)
                await self.extract_colors(page)
                await self.identify_primary_colors(page)
                await self.extract_typography(page)
                await self.extract_components(page)
                await self.extract_layout(page)

                # ---------- 交互与动效信息 ----------
                print("\n🎯 开始提取交互效果...")
                await self.extract_interactive_elements(page)
                await self.extract_hover_effects(page)
                await self.extract_click_effects(page)
                await self.extract_focus_effects(page)
                await self.extract_animations(page)
                await self.extract_transitions(page)
                await self.enable_safe_click_mode(page)
                await self.simulate_interactions(page)

                # ---------- 智能分析 ----------
                await self.detect_industry(page)
                await self.analyze_design_tokens(page)
                await self.take_screenshot(page)

                # ---------- 输出 ----------
                self.save_data()
                self.print_summary()

            finally:
                await browser.close()

    async def extract_css_variables(self, page):
        """提取 `:root` 中的 CSS 自定义属性（--token）。"""
        print("📌 提取 CSS 变量...")
        variables = await page.evaluate(
            """() => {
                const vars = {};
                const rootStyles = window.getComputedStyle(document.documentElement);
                const allProps = Array.from(rootStyles);
                const customProps = allProps.filter(prop => prop.startsWith('--'));
                customProps.forEach(prop => {
                    const value = rootStyles.getPropertyValue(prop).trim();
                    if (value) vars[prop] = value;
                });
                return vars;
            }"""
        )
        self.data["cssVariables"] = variables
        print(f"   找到 {len(variables)} 个 CSS 变量")

    async def extract_colors(self, page):
        """提取颜色系统并统计颜色出现频率。"""
        print("🎨 提取颜色系统...")
        color_data = await page.evaluate(
            """() => {
                const result = {
                    text: [],
                    background: [],
                    border: [],
                    gradients: [],
                    frequency: {},
                    allColors: []
                };
                const allElements = document.querySelectorAll('*');
                allElements.forEach(element => {
                    const style = window.getComputedStyle(element);
                    const info = {
                        tag: element.tagName.toLowerCase(),
                        class: element.className || '',
                        text: element.textContent?.substring(0, 50).trim() || ''
                    };

                    if (style.color && style.color !== 'rgba(0, 0, 0, 0)') {
                        result.text.push({ ...info, color: style.color });
                        result.allColors.push(style.color);
                    }
                    if (style.backgroundColor &&
                        style.backgroundColor !== 'rgba(0, 0, 0, 0)' &&
                        style.backgroundColor !== 'transparent') {
                        result.background.push({ ...info, color: style.backgroundColor });
                        result.allColors.push(style.backgroundColor);
                    }
                    if (style.borderColor &&
                        style.borderColor !== 'rgba(0, 0, 0, 0)' &&
                        style.borderColor !== 'transparent') {
                        result.border.push({ ...info, color: style.borderColor });
                        result.allColors.push(style.borderColor);
                    }
                    if (style.backgroundImage && style.backgroundImage.includes('gradient')) {
                        result.gradients.push({ ...info, gradient: style.backgroundImage });
                    }
                });
                result.allColors.forEach(c => {
                    result.frequency[c] = (result.frequency[c] || 0) + 1;
                });
                return result;
            }"""
        )

        self.data["colors"]["text"] = color_data["text"]
        self.data["colors"]["background"] = color_data["background"]
        self.data["colors"]["border"] = color_data["border"]
        self.data["colors"]["gradients"] = color_data["gradients"]
        self.data["colors"]["frequency"] = color_data["frequency"]

        print(f"   文本颜色: {len(color_data['text'])} 个")
        print(f"   背景颜色: {len(color_data['background'])} 个")
        print(f"   边框颜色: {len(color_data['border'])} 个")
        print(f"   渐变色: {len(color_data['gradients'])} 个")
        print(f"   颜色频率: {len(color_data['frequency'])} 种")

    async def identify_primary_colors(self, page):
        """基于常见命名语义（primary/secondary/accent）识别品牌主辅色。"""
        print("🎯 识别主色调...")
        colors = await page.evaluate(
            """() => {
                const x = { primary: null, secondary: null, accent: null };
                const primaryElements = document.querySelectorAll('[class*="primary"], [class*="brand"], .btn-primary, button.primary');
                const secondaryElements = document.querySelectorAll('[class*="secondary"], .btn-secondary, button.secondary');
                const accentElements = document.querySelectorAll('[class*="accent"], [class*="highlight"]');
                if (primaryElements.length) {
                    const s = window.getComputedStyle(primaryElements[0]);
                    x.primary = s.backgroundColor || s.color;
                }
                if (secondaryElements.length) {
                    const s = window.getComputedStyle(secondaryElements[0]);
                    x.secondary = s.backgroundColor || s.color;
                }
                if (accentElements.length) {
                    const s = window.getComputedStyle(accentElements[0]);
                    x.accent = s.backgroundColor || s.color;
                }
                return x;
            }"""
        )
        self.data["colors"]["primary"] = self.rgb_to_hex(colors["primary"])
        self.data["colors"]["secondary"] = self.rgb_to_hex(colors["secondary"])
        self.data["colors"]["accent"] = self.rgb_to_hex(colors["accent"])
        print(f"   主色调: {self.data['colors']['primary'] or '未识别'}")
        print(f"   次要色: {self.data['colors']['secondary'] or '未识别'}")
        print(f"   强调色: {self.data['colors']['accent'] or '未识别'}")

    async def extract_typography(self, page):
        """提取标题/段落/按钮中的字体家族、字号、字重、行高。"""
        print("📝 提取排版系统...")
        typography = await page.evaluate(
            """() => {
                const result = {
                    fonts: [], sizes: [], weights: [], lineHeights: [], fontFamilies: new Set()
                };
                const headings = document.querySelectorAll('h1,h2,h3,h4,h5,h6');
                const paragraphs = document.querySelectorAll('p');
                const buttons = document.querySelectorAll('button,.btn,[role="button"]');

                headings.forEach(h => {
                    const s = window.getComputedStyle(h);
                    const f = s.fontFamily.split(',')[0].replace(/['"]/g, '').trim();
                    result.fontFamilies.add(f);
                    result.fonts.push({
                        tag: h.tagName, fontFamily: s.fontFamily, fontSize: s.fontSize,
                        fontWeight: s.fontWeight, lineHeight: s.lineHeight,
                        color: s.color, text: h.textContent?.substring(0, 30)
                    });
                });

                paragraphs.forEach(p => {
                    if ((p.textContent || '').length < 20) return;
                    const s = window.getComputedStyle(p);
                    const f = s.fontFamily.split(',')[0].replace(/['"]/g, '').trim();
                    result.fontFamilies.add(f);
                    result.sizes.push({
                        fontFamily: s.fontFamily, fontSize: s.fontSize, fontWeight: s.fontWeight,
                        lineHeight: s.lineHeight, color: s.color, text: p.textContent?.substring(0, 30)
                    });
                });

                buttons.forEach(btn => {
                    const s = window.getComputedStyle(btn);
                    const f = s.fontFamily.split(',')[0].replace(/['"]/g, '').trim();
                    result.fontFamilies.add(f);
                });

                result.fontFamilies = Array.from(result.fontFamilies);
                return result;
            }"""
        )
        self.data["typography"] = typography
        print(f"   标题样式: {len(typography['fonts'])} 个")
        print(f"   段落样式: {len(typography['sizes'])} 个")
        print(f"   字体家族: {', '.join(typography['fontFamilies'])}")

    async def extract_components(self, page):
        """提取按钮、卡片、输入框、导航、链接组件样式。"""
        print("🔧 提取组件样式...")
        components = await page.evaluate(
            """() => {
                const result = { buttons: [], cards: [], inputs: [], navs: [], links: [], modals: [] };
                document.querySelectorAll('button,.btn,[role="button"],a.btn').forEach(el => {
                    const s = window.getComputedStyle(el);
                    result.buttons.push({
                        text: el.textContent?.substring(0, 20),
                        backgroundColor: s.backgroundColor, color: s.color, border: s.border,
                        borderRadius: s.borderRadius, padding: s.padding, fontSize: s.fontSize,
                        fontWeight: s.fontWeight, boxShadow: s.boxShadow, transition: s.transition
                    });
                });
                document.querySelectorAll('.card,[class*="card"],article,.article').forEach(el => {
                    const s = window.getComputedStyle(el);
                    result.cards.push({
                        backgroundColor: s.backgroundColor, border: s.border, borderRadius: s.borderRadius,
                        boxShadow: s.boxShadow, padding: s.padding, margin: s.margin, transition: s.transition
                    });
                });
                document.querySelectorAll('input,textarea,select').forEach(el => {
                    const s = window.getComputedStyle(el);
                    result.inputs.push({
                        type: el.type || el.tagName.toLowerCase(), backgroundColor: s.backgroundColor,
                        border: s.border, borderRadius: s.borderRadius, padding: s.padding,
                        fontSize: s.fontSize, color: s.color, transition: s.transition
                    });
                });
                document.querySelectorAll('nav,.nav,.navbar,header').forEach(el => {
                    const s = window.getComputedStyle(el);
                    result.navs.push({
                        backgroundColor: s.backgroundColor, height: s.height, padding: s.padding,
                        borderBottom: s.borderBottom, boxShadow: s.boxShadow
                    });
                });
                document.querySelectorAll('a:not(.btn)').forEach(el => {
                    const s = window.getComputedStyle(el);
                    result.links.push({
                        text: el.textContent?.substring(0, 20), color: s.color,
                        textDecoration: s.textDecoration, transition: s.transition
                    });
                });
                return result;
            }"""
        )
        self.data["components"] = components
        print(f"   按钮: {len(components['buttons'])} 个")
        print(f"   卡片: {len(components['cards'])} 个")
        print(f"   输入框: {len(components['inputs'])} 个")
        print(f"   导航: {len(components['navs'])} 个")
        print(f"   链接: {len(components['links'])} 个")

    async def extract_layout(self, page):
        """提取容器、网格和视口信息。"""
        print("📐 提取布局信息...")
        layout = await page.evaluate(
            """() => {
                const result = { containers: [], grids: [], spacing: [], viewport: { width: window.innerWidth, height: window.innerHeight } };
                document.querySelectorAll('.container,[class*="container"],main,.main,.wrapper').forEach(el => {
                    const s = window.getComputedStyle(el);
                    result.containers.push({ maxWidth: s.maxWidth, width: s.width, padding: s.padding, margin: s.margin });
                });
                document.querySelectorAll('[class*="grid"],[class*="flex"]').forEach(el => {
                    const s = window.getComputedStyle(el);
                    result.grids.push({
                        display: s.display, gridTemplateColumns: s.gridTemplateColumns, gap: s.gap,
                        justifyContent: s.justifyContent, alignItems: s.alignItems
                    });
                });
                return result;
            }"""
        )
        self.data["layout"] = layout
        print(f"   容器: {len(layout['containers'])} 个")
        print(f"   网格: {len(layout['grids'])} 个")

    async def extract_interactive_elements(self, page):
        """提取可交互元素清单，后续用于真实交互采样。"""
        print("🖱️ 提取可交互元素...")
        elements = await page.evaluate(
            """() => {
                const result = [];
                const selectors = [
                    'button', '.btn', '[role="button"]', 'a', 'input', 'textarea', 'select',
                    '[class*="clickable"]', '[class*="interactive"]', '.card', '[class*="card"]', 'article',
                    '[tabindex]', '[onclick]'
                ];
                const seen = new Set();
                selectors.forEach(selector => {
                    document.querySelectorAll(selector).forEach(el => {
                        const key = `${el.tagName}|${el.id}|${el.className}|${(el.textContent || '').slice(0, 30)}`;
                        if (seen.has(key)) return;
                        seen.add(key);
                        const s = window.getComputedStyle(el);
                        const rect = el.getBoundingClientRect();
                        result.push({
                            tag: el.tagName.toLowerCase(),
                            class: (typeof el.className === 'string'
                                ? el.className
                                : (el.className && typeof el.className.baseVal === 'string' ? el.className.baseVal : '')
                            ).substring(0, 50),
                            text: el.textContent?.substring(0, 30).trim(),
                            type: el.type || null,
                            href: el.href || null,
                            hasOnClick: !!el.onclick || el.hasAttribute('onclick'),
                            position: { x: rect.x, y: rect.y, width: rect.width, height: rect.height },
                            styles: {
                                cursor: s.cursor, transition: s.transition, animation: s.animation,
                                transform: s.transform, boxShadow: s.boxShadow, borderRadius: s.borderRadius
                            },
                            hasHover: s.cursor === 'pointer' || s.transition !== 'all 0s ease 0s',
                            hasClick: ['button', 'a'].includes(el.tagName.toLowerCase()) || !!el.onclick || el.hasAttribute('onclick'),
                            hasFocus: el.tabIndex >= 0 || ['input', 'textarea', 'select', 'button', 'a'].includes(el.tagName.toLowerCase())
                        });
                    });
                });
                return result;
            }"""
        )
        self.data["interactiveElements"] = elements
        print(f"   找到 {len(elements)} 个可交互元素")

    async def _extract_pseudo_effects(self, page, pseudo_selector, target_key):
        """通用伪类规则提取器，减少重复代码。"""
        effects = await page.evaluate(
            """({ pseudoSelector }) => {
                const effects = [];
                try {
                    for (const sheet of document.styleSheets) {
                        try {
                            const rules = sheet.cssRules || sheet.rules || [];
                            for (const rule of rules) {
                                if (!rule.selectorText || !rule.selectorText.includes(pseudoSelector)) continue;
                                const selector = rule.selectorText.replace(new RegExp(pseudoSelector.replace(':', '\\\\:'), 'g'), '').trim();
                                if (!selector) continue;
                                const elements = document.querySelectorAll(selector);
                                if (!elements.length) continue;
                                const el = elements[0];
                                const normal = window.getComputedStyle(el);
                                effects.push({
                                    selector: rule.selectorText,
                                    element: el.tagName.toLowerCase(),
                                    class: (typeof el.className === 'string'
                                        ? el.className
                                        : (el.className && typeof el.className.baseVal === 'string' ? el.className.baseVal : '')
                                    ).substring(0, 50),
                                    text: el.textContent?.substring(0, 20).trim(),
                                    ruleStyles: {
                                        backgroundColor: rule.style.backgroundColor || null,
                                        color: rule.style.color || null,
                                        transform: rule.style.transform || null,
                                        boxShadow: rule.style.boxShadow || null,
                                        borderColor: rule.style.borderColor || null,
                                        outline: rule.style.outline || null,
                                        opacity: rule.style.opacity || null
                                    },
                                    normalStyles: {
                                        backgroundColor: normal.backgroundColor,
                                        color: normal.color,
                                        transform: normal.transform,
                                        boxShadow: normal.boxShadow,
                                        borderColor: normal.borderColor,
                                        outline: normal.outline,
                                        opacity: normal.opacity
                                    }
                                });
                            }
                        } catch (e) {}
                    }
                } catch (e) {}
                return effects;
            }""",
            {"pseudoSelector": pseudo_selector},
        )
        self.data["interactions"][target_key] = effects
        print(f"   {pseudo_selector} 效果: {len(effects)} 个")

    async def extract_hover_effects(self, page):
        print("✨ 提取悬停效果...")
        await self._extract_pseudo_effects(page, ":hover", "hoverEffects")

    async def extract_click_effects(self, page):
        print("👆 提取点击效果...")
        await self._extract_pseudo_effects(page, ":active", "clickEffects")

    async def extract_focus_effects(self, page):
        print("🎯 提取焦点效果...")
        # 同时提取 :focus 与 :focus-visible，避免仅键盘可见焦点样式遗漏。
        await self._extract_pseudo_effects(page, ":focus", "focusEffects")
        focus_visible_effects = await page.evaluate(
            """() => {
                const effects = [];
                try {
                    for (const sheet of document.styleSheets) {
                        try {
                            const rules = sheet.cssRules || sheet.rules || [];
                            for (const rule of rules) {
                                if (!rule.selectorText || !rule.selectorText.includes(':focus-visible')) continue;
                                const selector = rule.selectorText.replace(/:focus-visible/g, '').trim();
                                if (!selector) continue;
                                const elements = document.querySelectorAll(selector);
                                if (!elements.length) continue;
                                const el = elements[0];
                                const normal = window.getComputedStyle(el);
                                effects.push({
                                    selector: rule.selectorText,
                                    element: el.tagName.toLowerCase(),
                                    class: (typeof el.className === 'string'
                                        ? el.className
                                        : (el.className && typeof el.className.baseVal === 'string' ? el.className.baseVal : '')
                                    ).substring(0, 50),
                                    text: el.textContent?.substring(0, 20).trim(),
                                    ruleStyles: {
                                        outline: rule.style.outline || null,
                                        boxShadow: rule.style.boxShadow || null,
                                        borderColor: rule.style.borderColor || null,
                                        opacity: rule.style.opacity || null
                                    },
                                    normalStyles: {
                                        outline: normal.outline,
                                        boxShadow: normal.boxShadow,
                                        borderColor: normal.borderColor,
                                        opacity: normal.opacity
                                    }
                                });
                            }
                        } catch (e) {}
                    }
                } catch (e) {}
                return effects;
            }"""
        )
        if focus_visible_effects:
            existing = self.data["interactions"]["focusEffects"]
            seen = {
                f"{item.get('selector','')}|{item.get('element','')}|{item.get('class','')}"
                for item in existing
            }
            for item in focus_visible_effects:
                key = f"{item.get('selector','')}|{item.get('element','')}|{item.get('class','')}"
                if key not in seen:
                    existing.append(item)
                    seen.add(key)
            print(f"   :focus-visible 效果: {len(focus_visible_effects)} 个")

    async def extract_animations(self, page):
        """提取元素动画与关键帧定义。"""
        print("🎬 提取动画效果...")
        animations = await page.evaluate(
            """() => {
                const result = [];
                const keyframes = {};
                try {
                    for (const sheet of document.styleSheets) {
                        try {
                            const rules = sheet.cssRules || sheet.rules || [];
                            for (const rule of rules) {
                                if (rule.type === CSSRule.KEYFRAMES_RULE) {
                                    keyframes[rule.name] = { name: rule.name, cssText: rule.cssText };
                                }
                            }
                        } catch (e) {}
                    }
                    document.querySelectorAll('*').forEach(el => {
                        const s = window.getComputedStyle(el);
                        if (!s.animation || s.animation === 'none') return;
                        result.push({
                            element: el.tagName.toLowerCase(),
                            class: (typeof el.className === 'string'
                                ? el.className
                                : (el.className && typeof el.className.baseVal === 'string' ? el.className.baseVal : '')
                            ).substring(0, 50),
                            text: el.textContent?.substring(0, 20).trim(),
                            animation: s.animation,
                            animationName: s.animationName,
                            animationDuration: s.animationDuration,
                            animationTimingFunction: s.animationTimingFunction,
                            animationDelay: s.animationDelay,
                            animationIterationCount: s.animationIterationCount,
                            keyframes: keyframes[s.animationName] || null
                        });
                    });
                } catch (e) {}
                return result;
            }"""
        )
        self.data["interactions"]["animations"] = animations
        print(f"   动画效果: {len(animations)} 个")

    async def extract_transitions(self, page):
        """提取具有过渡属性的元素，帮助复刻交互动效时长与缓动。"""
        print("🔄 提取过渡效果...")
        transitions = await page.evaluate(
            """() => {
                const result = [];
                const seen = new Set();
                document.querySelectorAll('*').forEach(el => {
                    const s = window.getComputedStyle(el);
                    if (!s.transition || s.transition === 'none' || s.transition === 'all 0s ease 0s') return;
                    const key = `${el.tagName}|${el.className}|${s.transition}`;
                    if (seen.has(key)) return;
                    seen.add(key);
                    result.push({
                        element: el.tagName.toLowerCase(),
                        class: (typeof el.className === 'string'
                            ? el.className
                            : (el.className && typeof el.className.baseVal === 'string' ? el.className.baseVal : '')
                        ).substring(0, 50),
                        text: el.textContent?.substring(0, 20).trim(),
                        transition: s.transition,
                        transitionProperty: s.transitionProperty,
                        transitionDuration: s.transitionDuration,
                        transitionTimingFunction: s.transitionTimingFunction,
                        transitionDelay: s.transitionDelay
                    });
                });
                return result;
            }"""
        )
        self.data["interactions"]["transitions"] = transitions
        print(f"   过渡效果: {len(transitions)} 个")

    async def enable_safe_click_mode(self, page):
        """
        启用安全点击模式。
        目的：真实采样时允许触发按下/抬起，但阻止默认跳转，避免页面离开导致采样中断。
        """
        print("🛡️ 启用安全点击模式...")
        await page.evaluate(
            """() => {
                if (!window.__styleExtractorClickGuard) {
                    window.__styleExtractorClickGuard = (event) => {
                        event.preventDefault();
                        event.stopPropagation();
                    };
                    document.addEventListener('click', window.__styleExtractorClickGuard, true);
                }
            }"""
        )

    async def simulate_interactions(self, page):
        """
        真实交互采样。

        采样策略：
        - 悬停采样：对元素 hover 前后比对样式变化。
        - 点击采样：mouse.down 采集 active 态，mouse.up 后采集 clicked 态。
        """
        print("🎭 模拟交互效果...")
        interaction_results = []
        simulated_hover_effects = []
        simulated_click_effects = []

        buttons = await page.query_selector_all("button, .btn, [role='button']")
        cards = await page.query_selector_all(".card, [class*='card'], article")
        links = await page.query_selector_all("a:not(.btn)")
        elements_to_test = (buttons[:4] + cards[:3] + links[:3])[:8]

        for element in elements_to_test:
            try:
                tag_name = await element.evaluate("el => el.tagName.toLowerCase()")
                class_name = await element.evaluate(
                    "el => ((typeof el.className === 'string' ? el.className : (el.className && typeof el.className.baseVal === 'string' ? el.className.baseVal : '')) || '').substring(0, 30)"
                )
                text = await element.evaluate("el => el.textContent?.substring(0, 20).trim() || ''")
                is_interactable = await element.evaluate(
                    """el => {
                        const r = el.getBoundingClientRect();
                        const s = window.getComputedStyle(el);
                        const disabled = el.hasAttribute('disabled') || el.getAttribute('aria-disabled') === 'true';
                        return (
                            r.width > 2 &&
                            r.height > 2 &&
                            s.display !== 'none' &&
                            s.visibility !== 'hidden' &&
                            s.pointerEvents !== 'none' &&
                            !disabled
                        );
                    }"""
                )
                if not is_interactable:
                    continue

                # 1) 采集初始样式
                normal_styles = await element.evaluate(
                    """el => {
                        const s = window.getComputedStyle(el);
                        return {
                            backgroundColor: s.backgroundColor,
                            color: s.color,
                            transform: s.transform,
                            boxShadow: s.boxShadow,
                            borderColor: s.borderColor,
                            opacity: s.opacity
                        };
                    }"""
                )

                # 2) 悬停采样
                try:
                    await element.evaluate(
                        """el => {
                            el.scrollIntoView({ block: 'center', inline: 'center', behavior: 'instant' });
                        }"""
                    )
                    await page.wait_for_timeout(80)
                    await element.hover(timeout=2500)
                    await page.wait_for_timeout(200)
                    hover_styles = await element.evaluate(
                        """el => {
                            const s = window.getComputedStyle(el);
                            return {
                                backgroundColor: s.backgroundColor,
                                color: s.color,
                                transform: s.transform,
                                boxShadow: s.boxShadow,
                                borderColor: s.borderColor,
                                opacity: s.opacity
                            };
                        }"""
                    )
                    hover_changes = {}
                    for key in normal_styles:
                        if normal_styles[key] != hover_styles[key]:
                            hover_changes[key] = {"from": normal_styles[key], "to": hover_styles[key]}
                    if hover_changes:
                        hover_result = {
                            "element": tag_name,
                            "class": class_name,
                            "text": text,
                            "type": "hover",
                            "changes": hover_changes,
                        }
                        interaction_results.append(hover_result)
                        simulated_hover_effects.append(hover_result)
                except Exception as hover_error:
                    print(f"   ⚠ 悬停采样跳过: {str(hover_error)[:70]}")

                # 3) 点击采样：active(按下态) + clicked(抬起后态)
                click_changes = {}
                clicked_state_changes = {}
                box = await element.bounding_box()
                if box and box.get("width", 0) > 2 and box.get("height", 0) > 2:
                    try:
                        x = box["x"] + box["width"] / 2
                        y = box["y"] + box["height"] / 2
                        await page.mouse.move(x, y)
                        await page.mouse.down()
                        await page.wait_for_timeout(100)
                        active_styles = await element.evaluate(
                            """el => {
                                const s = window.getComputedStyle(el);
                                return {
                                    backgroundColor: s.backgroundColor,
                                    color: s.color,
                                    transform: s.transform,
                                    boxShadow: s.boxShadow,
                                    borderColor: s.borderColor,
                                    opacity: s.opacity
                                };
                            }"""
                        )
                        for key in normal_styles:
                            if normal_styles[key] != active_styles[key]:
                                click_changes[key] = {"from": normal_styles[key], "to": active_styles[key]}

                        await page.mouse.up()
                        await page.wait_for_timeout(120)
                        clicked_styles = await element.evaluate(
                            """el => {
                                const s = window.getComputedStyle(el);
                                return {
                                    backgroundColor: s.backgroundColor,
                                    color: s.color,
                                    transform: s.transform,
                                    boxShadow: s.boxShadow,
                                    borderColor: s.borderColor,
                                    opacity: s.opacity
                                };
                            }"""
                        )
                        for key in normal_styles:
                            if normal_styles[key] != clicked_styles[key]:
                                clicked_state_changes[key] = {"from": normal_styles[key], "to": clicked_styles[key]}
                    except Exception as click_error:
                        print(f"   ⚠ 点击采样跳过: {str(click_error)[:70]}")

                if click_changes or clicked_state_changes:
                    click_result = {
                        "element": tag_name,
                        "class": class_name,
                        "text": text,
                        "type": "click",
                        "activeChanges": click_changes,
                        "clickedStateChanges": clicked_state_changes,
                    }
                    interaction_results.append(click_result)
                    simulated_click_effects.append(click_result)

                # 将鼠标移出，减少状态污染
                await page.mouse.move(0, 0)
                await page.wait_for_timeout(80)

            except Exception as e:
                print(f"   ⚠ 模拟交互失败: {str(e)[:80]}")

        self.data["interactions"]["simulatedHoverEffects"] = simulated_hover_effects
        self.data["interactions"]["simulatedClickEffects"] = simulated_click_effects
        self.data["interactions"]["simulatedInteractions"] = interaction_results
        print(f"   模拟悬停: {len(simulated_hover_effects)} 个")
        print(f"   模拟点击: {len(simulated_click_effects)} 个")
        print(f"   模拟交互总计: {len(interaction_results)} 个")

    async def detect_industry(self, page):
        """根据文本关键词与颜色特征做轻量行业识别。"""
        print("🏭 识别行业特征...")
        industry = await page.evaluate(
            """() => {
                const text = document.body.innerText.toLowerCase();
                const title = document.title.toLowerCase();
                const meta = document.querySelector('meta[name="description"]')?.content.toLowerCase() || '';
                const content = `${text} ${title} ${meta}`;

                const indicators = {
                    tech: ['api','developer','code','programming','software','github','documentation','ai','data'],
                    food: ['food','restaurant','menu','delivery','order','chef','kitchen'],
                    medical: ['hospital','doctor','medical','health','clinic','patient','treatment'],
                    education: ['education','course','student','teacher','learn','school','training','tutorial'],
                    government: ['government','policy','service','public','official'],
                    architecture: ['architecture','building','project','construction','design studio']
                };
                const scores = {};
                let best = 'tech';
                let max = 0;
                for (const [name, words] of Object.entries(indicators)) {
                    scores[name] = 0;
                    for (const w of words) if (content.includes(w)) scores[name] += 1;
                    if (scores[name] > max) {
                        max = scores[name];
                        best = name;
                    }
                }
                return { type: best, confidence: max > 5 ? 'high' : max > 2 ? 'medium' : 'low', scores };
            }"""
        )
        self.data["industry"] = industry
        print(f"   识别行业: {industry['type']} (置信度: {industry['confidence']})")

    async def analyze_design_tokens(self, page):
        """从 CSS 变量中分拣颜色、间距、圆角、阴影、过渡等设计令牌。"""
        print("🧩 分析设计令牌...")
        tokens = await page.evaluate(
            """() => {
                const tokens = { colors: {}, spacing: {}, borderRadius: {}, shadows: {}, transitions: {} };
                const rootStyles = window.getComputedStyle(document.documentElement);
                const allProps = Array.from(rootStyles).filter(p => p.startsWith('--'));
                allProps.forEach(prop => {
                    const value = rootStyles.getPropertyValue(prop).trim();
                    if (!value) return;
                    if (value.includes('#') || value.includes('rgb')) tokens.colors[prop] = value;
                    else if (value.includes('px') && /(spacing|space|gap|padding|margin)/i.test(prop)) tokens.spacing[prop] = value;
                    else if (value.includes('px') && /(radius|corner)/i.test(prop)) tokens.borderRadius[prop] = value;
                    else if (/(shadow|box-shadow)/i.test(value) || /(shadow)/i.test(prop)) tokens.shadows[prop] = value;
                    else if (/(transition|duration|ease)/i.test(value) || /(transition|duration)/i.test(prop)) tokens.transitions[prop] = value;
                });
                return tokens;
            }"""
        )
        self.data["designTokens"] = tokens
        print(f"   颜色令牌: {len(tokens['colors'])} 个")
        print(f"   间距令牌: {len(tokens['spacing'])} 个")
        print(f"   圆角令牌: {len(tokens['borderRadius'])} 个")

    async def take_screenshot(self, page):
        """保存完整页面截图，用于人工校验提取准确性。"""
        print("📸 截取页面截图...")
        assets_dir = self.output_dir / "assets"
        assets_dir.mkdir(parents=True, exist_ok=True)
        screenshot_path = assets_dir / "page-screenshot.png"
        await page.screenshot(path=str(screenshot_path), full_page=True)
        self.data["screenshot"] = str(screenshot_path)
        print(f"   截图已保存: {screenshot_path}")

    def save_data(self):
        """将采集结果保存为 `page-info.json` 与 `extraction-summary.txt`。"""
        assets_dir = self.output_dir / "assets"
        assets_dir.mkdir(parents=True, exist_ok=True)

        data_path = assets_dir / "page-info.json"
        with open(data_path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)
        print(f"\n📄 数据已保存: {data_path}")

        summary_path = assets_dir / "extraction-summary.txt"
        with open(summary_path, "w", encoding="utf-8") as f:
            f.write(self.generate_summary())
        print(f"📄 摘要已保存: {summary_path}")

    def generate_summary(self):
        """生成可读摘要，便于快速检查提取结果是否达标。"""
        summary = "=== 页面信息提取摘要（统一完整版） ===\n\n"
        summary += f"URL: {self.data['url']}\n"
        summary += f"时间: {self.data['timestamp']}\n"
        industry = self.data["industry"] or {"type": "未识别", "confidence": "未知"}
        summary += f"行业: {industry['type']} ({industry['confidence']} 置信度)\n\n"
        summary += "=== 颜色系统 ===\n"
        summary += f"主色调: {self.data['colors']['primary'] or '未识别'}\n"
        summary += f"次要色: {self.data['colors']['secondary'] or '未识别'}\n"
        summary += f"强调色: {self.data['colors']['accent'] or '未识别'}\n"
        summary += f"颜色样本: {len(self.data['colors']['frequency'])} 种\n\n"
        summary += "=== 交互效果 ===\n"
        summary += f"悬停规则: {len(self.data['interactions']['hoverEffects'])} 个\n"
        summary += f"点击规则: {len(self.data['interactions']['clickEffects'])} 个\n"
        summary += f"焦点规则: {len(self.data['interactions']['focusEffects'])} 个\n"
        summary += f"动画效果: {len(self.data['interactions']['animations'])} 个\n"
        summary += f"过渡效果: {len(self.data['interactions']['transitions'])} 个\n"
        summary += f"模拟悬停: {len(self.data['interactions']['simulatedHoverEffects'])} 个\n"
        summary += f"模拟点击: {len(self.data['interactions']['simulatedClickEffects'])} 个\n"
        summary += f"模拟交互总计: {len(self.data['interactions']['simulatedInteractions'])} 个\n\n"
        summary += "=== 其他 ===\n"
        summary += f"CSS变量: {len(self.data['cssVariables'])} 个\n"
        summary += f"可交互元素: {len(self.data['interactiveElements'])} 个\n"
        return summary

    def print_summary(self):
        """终端摘要输出。"""
        print("\n✅ 页面信息提取完成！\n")
        print("📊 提取摘要:")
        print(f"   主色调: {self.data['colors']['primary'] or '未识别'}")
        print(f"   次要色: {self.data['colors']['secondary'] or '未识别'}")
        print(f"   CSS变量: {len(self.data['cssVariables'])} 个")
        print(f"   颜色样本: {len(self.data['colors']['frequency'])} 种")
        print(f"   交互元素: {len(self.data['interactiveElements'])} 个")
        print(f"   悬停效果: {len(self.data['interactions']['hoverEffects'])} 个")
        print(f"   点击效果: {len(self.data['interactions']['clickEffects'])} 个")
        print(f"   模拟点击: {len(self.data['interactions']['simulatedClickEffects'])} 个")
        print(f"   动画效果: {len(self.data['interactions']['animations'])} 个")


def main():
    """命令行入口。"""
    parser = argparse.ArgumentParser(
        description="提取页面设计与交互信息并输出为结构化文件。"
    )
    parser.add_argument(
        "--url",
        required=True,
        help="目标页面 URL（必填）",
    )
    parser.add_argument(
        "--output_dir",
        default=str(Path.cwd() / "output"),
        help="输出目录，默认当前目录下 output/",
    )
    args = parser.parse_args()

    extractor = PageExtractor(args.url, args.output_dir)
    asyncio.run(extractor.extract())


if __name__ == "__main__":
    main()
