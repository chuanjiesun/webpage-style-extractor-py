---
name: bestblogs-design
description: 提取并应用 BestBlogs 的设计风格与配色方案，适用于科技/内容平台行业网站页面设计。包含墨蓝色品牌色系、琥珀色强调色、Geist字体排版规范、卡片组件和阅读工作流布局指南。
meta:
  - "industry: tech"
  - "category: content-platform"
---

# BestBlogs 设计风格指南

## 概述

BestBlogs 是一个以"发现优质内容"为核心的 AI 驱动阅读平台，设计风格沉稳内敛，以墨蓝色（Ink #1A365D）为品牌主色，搭配琥珀色（Amber #D97706）作为关键强调色，营造出编辑精选的权威感与温暖阅读氛围。页面采用奶油白/暖白底色，大量留白配合精致卡片布局，让内容本身成为视觉焦点。

**行业定位**：科技 / 内容平台
**设计风格**：现代、沉稳、书卷气
**核心特点**：
- 墨蓝色品牌色（#1A365D）+ 琥珀色强调（#D97706）双色调
- 奶油白暖底色（#FEFDFB）营造阅读氛围
- 精致的卡片阴影（墨蓝色调，非纯黑色调）
- Geist 现代字体 + 系统中文回退
- 微交互过渡统一（0.15s / 0.2s cubic-bezier）

## 色彩系统

### 主色调

**品牌主色（Ink 墨蓝）**：`#1A365D` (RGB: 26, 54, 93)
- CSS变量：`--primary: 26 54 93`、`--color-ink: 26 54 93`
- 用于：品牌文字、CTA 按钮背景、导航强调
- 传达：权威、专业、可信
- 行业特征：深墨蓝区别于科技行业常见的亮蓝/紫色，更契合内容平台的编辑权威感

### 辅助色

**次要颜色**：
- `#B45309` - 深琥珀，用于 Pro 标签、付费标识
- `#2C5282` - 浅墨蓝（Ink Light），用于链接悬停色
- `#1A202C` - 墨蓝深色（Ink Dark），用于更深强调

### 文字颜色

**文本色系**：
- 主标题：`#1A365D` - Ink 墨蓝，区块主标题
- 正文标题：`#1E293B` - Slate 800，卡片标题、文章标题
- 正文：`#64748B` - Slate 500，段落文本
- 辅助文本：`#94A3B8` - Slate 400，次要说明
- 链接默认：`#1A365D` - 与主标题同色
- 链接悬停：`#2C5282` - Ink Light，较亮的蓝色
- 琥珀标签文字：`#B45309` / `rgba(180, 83, 9, 0.8)` - 功能说明标题

### 强调色与功能色

**强调色**：
- CTA按钮背景：`#1A365D`（Ink 墨蓝）
- 品牌标签/Pro：`#D97706`（琥珀色 Amber）
- 品牌高亮文字：`#F59E0B`（Amber 浅色）
- 功能标题：`rgba(180, 83, 9, 0.8)` - 半透明深琥珀

**功能色**（基于 CSS 变量定义）：
- 成功：`#059669` (`--color-success: 5 150 105`)
- 成功淡底：`#D1FAE5` (`--color-success-muted: 209 250 229`)
- 错误：`#DC2626` (`--color-error: 220 38 38`)
- 错误淡底：`#FEE2E2` (`--color-error-muted: 254 226 226`)
- 警告：`#D97706` (`--color-warning: 217 119 6`)
- 警告淡底：`#FEF3C7` (`--color-warning-muted: 254 243 199`)
- 信息：`#0284C7` (`--color-info: 2 132 199`)
- 信息淡底：`#E0F2FE` (`--color-info-muted: 224 242 254`)

### 渐变色

**Hero 区顶部渐变**：
```css
background: linear-gradient(rgba(255, 251, 235, 0.4), #FEFDFB, #FEFDFB);
```
- 方向：从上到下
- 起点色：`rgba(255, 251, 235, 0.4)`（淡琥珀暖光）
- 终点色：`#FEFDFB`（页面主底色）
- 作用：在 Hero 区顶部营造微暖光晕

**Amber 径向渐变**（装饰光晕）：
```css
background: radial-gradient(rgba(217, 119, 6, 0.06) 0%, rgba(0, 0, 0, 0) 70%);
```
- 作用：页面中央微弱的琥珀色光晕装饰

**卡片装饰渐变**：
```css
background: linear-gradient(to right bottom, rgba(253, 230, 138, 0.2), rgba(0, 0, 0, 0));
```
- 方向：从左上到右下
- 起点色：`rgba(253, 230, 138, 0.2)`（淡琥珀色）
- 终点色：透明

**底部区块渐变**：
```css
background: linear-gradient(rgba(241, 245, 249, 0.3), rgba(255, 251, 235, 0.3));
```
- 方向：从上到下
- 起点色：`rgba(241, 245, 249, 0.3)`（淡灰蓝）
- 终点色：`rgba(255, 251, 235, 0.3)`（淡琥珀暖色）

### 背景色调

- `#FEFDFB` - 页面主底色（Paper 奶油白），CSS变量 `--bg-paper`
- `#FAF7F2` - 暖纸色（Paper Cream），CSS变量 `--bg-paper-cream`
- `#FDFAF6` - 温暖白色（Paper Warm），CSS变量 `--bg-paper-warm`
- `#FFFFFF` - 卡片/弹出层白色，CSS变量 `--card`
- `#F8FAFC` - 微灰底色（Subtle），CSS变量 `--bg-subtle`
- `#F1F5F9` - 灰底（Muted），CSS变量 `--muted` / `--bg-muted`

### 边框颜色

- `#E2E8F0` - 默认边框（Border Default），CSS变量 `--border`
- `#F1F5F9` - 柔和边框（Border Muted），CSS变量 `--border-muted`
- `#CBD5E1` - 强调边框（Border Emphasis），CSS变量 `--border-emphasis`
- `rgba(26, 54, 93, 0.2)` - 悬停边框（Ink/20）
- `rgba(26, 54, 93, 0.3)` - 卡片悬停边框（Ink/30）

## 排版系统

### 字体家族

**主字体**：Geist
- CSS变量：`--font-geist: "Geist", PingFang SC, Hiragino Sans GB, Microsoft YaHei, Noto Sans SC, system-ui, -apple-system, sans-serif`
- 后备字体：PingFang SC (macOS中文)、Hiragino Sans GB、Microsoft YaHei (Windows中文)、Noto Sans SC

**等宽字体**：Geist Mono
- CSS变量：`--font-geist-mono: "Geist Mono", JetBrains Mono, Fira Code, SF Mono, Consolas, Liberation Mono, monospace`
- 用于：代码块、技术内容

**装饰字体**：Georgia
- 实际出现在引用/特殊段落中
- 用于：引言、编辑推荐语等特殊文本

### 字号层级

| 层级 | 字号 | 行高 | 字重 | 应用场景 |
|------|------|------|------|----------|
| Hero 标题 | 44px | 44px | 700 | 页面主标题（Discover quality content...） |
| CTA 区标题 | 38px | 44px | 700 | 底部号召区标题（Stop scrolling. Start reading.） |
| 区块标题 | 30px | 36px | 700 | 各区块大标题（Why BestBlogs 等） |
| Tab 标题 | 24px | 32px | 700 | 功能标签标题（Explore / My Brief / For You） |
| 文章卡片标题 | 20px | 28px | 600 | 大卡片文章标题 |
| 区块副标题 | 18px | 28px | 700 | 功能要点标题（Not the same...） |
| 功能描述标题 | 18px | 28px | 600 | 功能模块标签（Free / Pro） |
| 正文 | 16px | 26px | 400 | 段落文本 |
| 辅助正文 | 14px | 22.75px | 400 | 功能说明文字 |
| 功能点标题 | 14px | 20px | 500 | 小标题（Start with...） |
| 导航链接 | 14px | 20px | 500 | 顶部导航 |
| 小标签 | 14px | 20px | 600 | 底部导航（Start Reading 等） |

### 字重与行高

**字重规范**：
- 粗体（700）：主标题、区块标题、强调文字
- 半粗（600）：卡片标题、功能标签、导航
- 中等（500）：功能点标题、导航链接、琥珀标签文字
- 常规（400）：正文、描述

**行高规范**：
- 大标题：1.0（44px/44px）、1.16（44px/38px）
- 区块标题：1.2（36px/30px）
- Tab 标题：1.33（32px/24px）
- 正文：1.625（26px/16px）
- 小字：1.625（20px/14px 辅助）、1.43（20px/14px 导航）

## 组件样式

### 卡片组件

**主内容卡片**：
```css
.card {
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 12px;
  box-shadow:
    0 0 0 0 rgba(0, 0, 0, 0),
    0 0 0 0 rgba(0, 0, 0, 0),
    rgba(26, 54, 93, 0.05) 0px 10px 15px -3px,
    rgba(26, 54, 93, 0.05) 0px 4px 6px -2px;
  transition:
    color 0.15s cubic-bezier(0.4, 0, 0.2, 1),
    background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1),
    border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1);
}

.card:hover {
  border-color: rgba(26, 54, 93, 0.3);
  box-shadow: var(--shadow-card-hover);
}
```

**功能卡片**（Why BestBlogs 区块）：
```css
.feature-card {
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 12px;
  padding: 32px;
  box-shadow: none;
  transition:
    color 0.15s cubic-bezier(0.4, 0, 0.2, 1),
    background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1),
    border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1);
}
```

**Hero 区大卡片**：
```css
.hero-card {
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 12px;
  box-shadow:
    0 0 0 0 rgba(0, 0, 0, 0),
    0 0 0 0 rgba(0, 0, 0, 0),
    rgba(26, 54, 93, 0.1) 0px 25px 50px -12px;
}
```

**文章列表卡片**：
```css
.article-card {
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 12px;
  box-shadow:
    0 0 0 0 rgba(0, 0, 0, 0),
    0 0 0 0 rgba(0, 0, 0, 0),
    rgb(255, 255, 255) 0px 1px 3px 0px,
    rgb(255, 255, 255) 0px 1px 2px -1px;
  transition: 0.15s cubic-bezier(0.4, 0, 0.2, 1);
}

.article-card:hover {
  border-color: rgba(26, 54, 93, 0.3);
  box-shadow: var(--shadow-card-hover);
}
```

### 按钮组件

**主 CTA 按钮**：
```css
.btn-primary {
  background: #1A365D;
  color: #FFFFFF;
  border-radius: 8px;
  height: 48px;
  font-weight: 500;
  box-shadow:
    rgba(26, 54, 93, 0.1) 0px 10px 15px -3px,
    rgba(26, 54, 93, 0.1) 0px 4px 6px -2px;
  transition:
    color 0.2s cubic-bezier(0.4, 0, 0.2, 1),
    background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1),
    border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

.btn-primary:hover {
  background: rgba(26, 54, 93, 0.9);
  color: #FFFFFF;
}
```

**次要按钮**（Change language / Switch Theme）：
```css
.btn-secondary {
  background: transparent;
  color: #1E293B;
  border: 1px solid #E2E8F0;
  border-radius: 6px;
  font-weight: 500;
  transition:
    color 0.2s cubic-bezier(0.4, 0, 0.2, 1),
    background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1),
    border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

.btn-secondary:hover {
  background: #F1F5F9;
}
```

### 导航组件

**顶部导航栏**：
```css
.navbar {
  position: sticky;
  top: 0;
  z-index: 20;
  background: transparent;
  height: 57px;
  width: 100%;
  border-bottom: 1px solid transparent;
}
```

**导航链接**：
```css
.nav-link {
  color: #64748B;
  font-size: 14px;
  font-weight: 500;
  text-decoration: none;
  padding: 6px 12px;
  border-radius: 6px;
  transition:
    color 0.15s cubic-bezier(0.4, 0, 0.2, 1),
    background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1);
}

.nav-link:hover {
  color: #1E293B;
  background: #F1F5F9;
}
```

### 文字链接

```css
.text-link {
  color: #1A365D;
  text-decoration: none;
  transition:
    color 0.15s cubic-bezier(0.4, 0, 0.2, 1),
    background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1);
}

.text-link:hover {
  color: #2C5282;
}

.text-link:visited {
  color: #1A365D;
}
```

### 标签组件

**PUBLIC PICKS 标签**：使用绿色 SVG 图标 + 文字
**Pro 标签**：`color: #B45309; font-weight: 600;`
**Free 标签**：`color: #1E293B; font-weight: 600;`
**琥珀色功能标题**：`color: rgba(180, 83, 9, 0.8); font-weight: 500;`

## 布局与间距

### 网格系统

**文章卡片网格**：
- 桌面端：12列 grid，gap 由内容自适应
- 使用 Tailwind CSS grid 工具类

### 断点设置

- 移动端：< 640px（默认）
- 平板端：640px - 1023px（`md:` 前缀）
- 桌面端：≥ 1024px（`lg:` 前缀）
- 大屏：≥ 1280px

### 间距系统

| 名称 | 值 | 应用场景 |
|------|-----|----------|
| xs | 4px | 微小间距（gap-1） |
| sm | 8px | 圆角默认值（--radius: .5rem）、小组间距 |
| md | 12px | 导航链接内边距（px-3） |
| lg | 16px | 按钮内边距（py-4）、区块内间距 |
| xl | 24px | 区块间距（py-6）、标题间距 |
| 2xl | 32px | 功能卡片内边距（p-8）、按钮内间距 |
| 3xl | 48px | 大区块间距 |
| 4xl | 80px | 大区块外间距（py-20） |
| 5xl | 112px | 大屏区块外间距（md:py-28） |

### 容器设置

```css
.container {
  max-width: 1265px;
  margin: 0 auto;
  width: 100%;
}
```

## 特效与交互

### 过渡效果

```css
/* 链接/文字过渡 - 快速 */
transition:
  color 0.15s cubic-bezier(0.4, 0, 0.2, 1),
  background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1),
  border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1),
  text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1),
  fill 0.15s cubic-bezier(0.4, 0, 0.2, 1),
  stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1);

/* 按钮/CTA 过渡 - 标准 */
transition:
  color 0.2s cubic-bezier(0.4, 0, 0.2, 1),
  background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1),
  border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1),
  text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1),
  fill 0.2s cubic-bezier(0.4, 0, 0.2, 1),
  stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1);

/* 变换过渡 */
transition: transform 0.15s cubic-bezier(0.4, 0, 0.2, 1);
```

### 悬停效果

- 导航链接：颜色从 `#64748B` 变为 `#1E293B`，背景变为 `#F1F5F9`
- 文字链接：颜色从 `#1A365D` 变为 `#2C5282`，出现下划线
- CTA 按钮：背景从 `#1A365D` 变为 `rgba(26, 54, 93, 0.9)`
- 文章卡片：边框从 `#E2E8F0` 变为 `rgba(26, 54, 93, 0.3)`，阴影增强
- 功能卡片：边框从 `#E2E8F0` 变为 `rgba(26, 54, 93, 0.2)`
- 卡片标题：组悬停时颜色从 `#1E293B` 变为 `#1A365D`（Ink）

### 点击效果

- 按钮与链接在交互后颜色变化保持与悬停态一致
- 无额外偏移或缩放效果

### 焦点效果

- Skip 链接焦点：`background: #1A365D; color: #FFFFFF; border-radius: 6px; position: absolute; top: 16px; left: 16px; z-index: 50;` + `box-shadow` 阴影
- 通用焦点：`outline: none; box-shadow: ring 偏移 2px + ring(2px) rgba(26,54,93,0.4) + offset-paper`

## 行业特色设计

### 内容平台行业特有元素

**行业色彩规范**：
- 墨蓝色（#1A365D）作为品牌主色，传达编辑精选的权威感，区别于科技行业常见亮蓝
- 琥珀色（#D97706）作为强调色，用于 Pro 标识、功能亮点，传达温暖与品质感
- 奶油白底色（#FEFDFB），营造纸质阅读感
- 微暖渐变装饰，琥珀色光晕，增加阅读温度

**行业组件**：
- PUBLIC PICKS 标签：绿色圆点 + 文字，编辑精选标识
- Pro / Free 标签：琥珀色 vs 深色文字，付费区隔
- 文章卡片：标题 + 来源 + 摘要，三层信息结构
- 功能三步骤：01 Explore → 02 My Brief → 03 For You，分步引导
- 阅读工作流 Tab：Explore / My Brief / For You / AI Copilot

**行业布局特点**：
- Hero 区顶部琥珀色微光渐变，底部奶油白
- 内容展示以卡片网格为主，4列或自适应
- 底部 CTA 区使用大标题 + 单一按钮，简洁有力
- 琥珀色功能标题 + 灰色说明文字，形成视觉层级

## 使用建议

### 适用场景

- ✅ 内容聚合平台官网
- ✅ 阅读/知识管理工具落地页
- ✅ 编辑精选/策展类产品页
- ✅ 科技博客/媒体网站
- ✅ 付费内容 SaaS 产品页

### 避免场景

- ❌ 娱乐/短视频类网站（色调过于沉稳）
- ❌ 电商购物网站（缺少购买引导视觉刺激）
- ❌ 游戏平台（品牌色不够活泼）

### 最佳实践

1. 保持墨蓝（#1A365D）+ 琥珀（#D97706）双色调体系，不引入第三种强调色
2. 卡片阴影使用品牌墨蓝色调（rgba(26,54,93,0.05)），而非纯黑，保持品牌一致性
3. 底色使用奶油白（#FEFDFB）而非纯白，营造纸张阅读感
4. 所有过渡统一使用 `cubic-bezier(0.4, 0, 0.2, 1)` 缓动，链接 0.15s、按钮 0.2s
5. 中文排版确保 PingFang SC / Microsoft YaHei / Noto Sans SC 回退链完整

## CSS变量参考

```css
:root {
  /* 品牌色 */
  --color-ink: 26 54 93;
  --color-ink-dark: 26 32 44;
  --color-ink-light: 44 82 130;
  --primary: 26 54 93;
  --primary-foreground: 255 255 255;

  /* 琥珀强调色 */
  --accent: 217 119 6;
  --accent-foreground: 255 255 255;
  --color-amber: 217 119 6;
  --color-amber-light: 245 158 11;
  --color-amber-muted: 254 243 199;

  /* 文字颜色 */
  --foreground: 30 41 59;
  --text-primary: 30 41 59;
  --text-secondary: 71 85 105;
  --text-tertiary: 100 116 139;
  --text-muted: 148 163 184;
  --text-placeholder: 203 213 225;
  --color-link: 26 54 93;
  --color-link-hover: 44 82 130;

  /* 背景颜色 */
  --background: 254 253 251;
  --bg-paper: 254 253 251;
  --bg-paper-cream: 250 247 242;
  --bg-paper-warm: 253 250 246;
  --bg-subtle: 248 250 252;
  --bg-muted: 241 245 249;
  --bg-surface: 255 255 255;
  --bg-surface-raised: 255 255 255;
  --card: 255 255 255;
  --card-foreground: 30 41 59;
  --muted: 241 245 249;
  --muted-foreground: 100 116 139;
  --secondary: 241 245 249;
  --secondary-foreground: 30 41 59;
  --popover: 255 255 255;
  --popover-foreground: 30 41 59;

  /* 边框 */
  --border: 226 232 240;
  --border-default: 226 232 240;
  --border-muted: 241 245 249;
  --border-emphasis: 203 213 225;
  --input: 226 232 240;

  /* 功能色 */
  --color-success: 5 150 105;
  --color-success-muted: 209 250 229;
  --color-error: 220 38 38;
  --color-error-muted: 254 226 226;
  --color-warning: 217 119 6;
  --color-warning-muted: 254 243 199;
  --color-info: 2 132 199;
  --color-info-muted: 224 242 254;
  --destructive: 220 38 38;
  --destructive-foreground: 255 255 255;

  /* 焦点 */
  --focus-ring: 26 54 93 / .4;
  --ring: 26 54 93;

  /* 圆角 */
  --radius: .5rem;

  /* 字体 */
  --font-geist: "Geist", PingFang SC, Hiragino Sans GB, Microsoft YaHei, Noto Sans SC, system-ui, -apple-system, sans-serif;
  --font-geist-mono: "Geist Mono", JetBrains Mono, Fira Code, SF Mono, Consolas, Liberation Mono, monospace;
}
```

## 设计原则总结

1. **品牌双色调**：墨蓝（#1A365D）+ 琥珀（#D97706），一个传达权威感、一个传达温度感，形成独特的阅读平台视觉识别
2. **纸质阅读感**：奶油白底色（#FEFDFB）、暖光渐变、精致留白，模拟纸质阅读体验
3. **品牌色阴影**：卡片阴影使用品牌墨蓝色调（rgba(26,54,93,0.05~0.1)）而非纯黑，品牌一致性贯穿微细节
4. **分步引导叙事**：Explore → My Brief → For You → AI Copilot，用编号步骤引导用户理解工作流
5. **克制交互**：过渡效果统一且克制（0.15s/0.2s），状态变化以颜色为主，无复杂动画

---

**最后更新时间**：2026-04-16
**版本**：1.0.0
**行业**：科技 / 内容平台
