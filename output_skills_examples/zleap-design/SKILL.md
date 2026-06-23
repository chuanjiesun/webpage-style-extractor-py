---
name: zleap-design
description: 提取并应用 Zleap 下一代内容社区的设计风格与配色方案，适用于科技/社交媒体类网站页面设计。包含完整的色彩系统、排版规范、组件样式和布局指南。
meta:
  - "industry: tech"
  - "category: social-content-platform"
---

# Zleap 设计风格指南

## 概述

Zleap 是一个面向下一代的内容社区平台，定位「人与Agent共同创作和交流」。页面采用极简主义设计，以大面积留白结合浅灰背景打造清爽的阅读体验。橙色（#FF8A00）作为品牌强调色贯穿全站，配合圆角化 UI 元素和细腻的过渡动效，营造现代、友好、轻量的视觉感受。

**行业定位**：科技 / 社交媒体内容平台
**设计风格**：极简现代
**核心特点**：
- 橙色强调色（#FF8A00）贯穿品牌触点
- 全圆角 UI 组件，亲和力强
- 系统字体栈，跨平台一致
- 浅灰底色（#F5F5F5）+ 白色卡片，层次分明
- 0.15s cubic-bezier 过渡，交互细腻
- 头像采用绿→黄暖系渐变

## 色彩系统

### 主色调

**品牌主色**：`#FF8A00` (RGB: 255, 138, 0)
- 用于：CTA按钮、关注按钮、登录入口、边框强调
- 传达：活力、温暖、行动号召
- 行业特征：科技平台中罕见使用橙色作为主色，差异化识别度高

### 辅助色

**次要颜色**：
- `#F5F5F5` - 页面全局底色，用于最外层容器背景
- `#F4F4F5` - 导航选中态及悬停态背景
- `#F9FAFB` - 文章卡片悬停背景
- `#FFFFFF` - 卡片、导航栏、内容区背景

### 文字颜色

**文本色系**：
- 标题：`#0F1419` - 文章主标题，深色高对比度
- 用户名：`#171717` - 用户名称，中等深色
- 正文：`#0F1419` - 文章摘要文本
- 辅助文本：`#525252` - 操作按钮文本（点赞/收藏/分享）
- 弱化文本：`#A1A1AA` - 时间戳、次要标签
- 导航链接：`#44403C` - 顶部导航及侧栏非激活项
- 侧栏选中：`#292524` - 发现/关注切换选中态

### 强调色与功能色

**强调色**：
- CTA按钮：`#FF8A00`
- 高亮：`#292524`

**功能色**：
- 成功：`#10B981`
- 错误：`#EF4444`
- 警告：`#F59E0B`
- 信息：`#3B82F6`

### 渐变色

**头像渐变**：`linear-gradient(to bottom right, #92D8C2, #F6D365)`
- 从薄荷绿到暖黄色，用于用户默认头像
- 搭配暖金阴影：`shadow-[0_0_10.67px_5.33px_rgba(255,232,163,0.80)]`
- 仅用于头像组件，作为视觉暖色点缀

## 排版系统

### 字体家族

**主字体**：系统默认无衬线字体
- CSS: `font-family: ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";`
- 后备字体：系统字体自动匹配

**等宽字体**：
- CSS: `font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;`

### 字号层级

| 层级 | 字号 | 行高 | 字重 | 应用场景 |
|------|------|------|------|----------|
| 文章标题 | 17px | 20px | 800 | 信息流文章主标题 |
| 正文 | 15px | 20px | 400 | 文章摘要/正文片段 |
| 区块标题 | 16px | 24px | 500 | 侧边栏区块标题（H3） |
| 用户名 | 16px | 22px | 500 | 文章作者名 |
| 按钮文本 | 16px | 22px | 400-500 | 导航/操作按钮 |
| 操作文本 | 14px | 20px | 400 | 点赞、收藏、分享按钮 |
| 时间戳 | 14px | 20px | 400 | 发布时间、元信息 |

### 字重与行高

**字重规范**：
- 超粗体（800）：文章标题（`font-extrabold`）
- 中等（500）：用户名、区块标题、选中导航（`font-medium`）
- 常规（400）：正文、操作文本、时间戳、导航（`font-normal`）

**行高规范**：
- 标题：20px（紧凑，1.18倍）
- 正文：20px（紧凑，1.33倍）
- 区块标题：24px（1.5倍）
- 用户名/导航：22px（1.375倍）

## 组件样式

### 卡片组件

**文章卡片**：
```css
.article-card {
  cursor: pointer;
  border-radius: 4px;
  padding: 32px 20px 0;
  transition: background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1);
}
.article-card:first-child {
  padding-top: 24px;
}
.article-card:hover {
  background-color: #F9FAFB;
}
```

**内容预览卡片**（文章内嵌媒体卡）：
```css
.content-preview-card {
  margin-top: 8px;
  overflow: hidden;
  border-radius: 12px;
  border: 1px solid rgb(239, 243, 244);
}
.content-preview-card .media-area {
  position: relative;
  aspect-ratio: 5/2;
  width: 100%;
  overflow: hidden;
}
.content-preview-card .text-area {
  padding: 12px;
}
```

### 按钮组件

**主CTA按钮（登录）**：
```css
.btn-cta {
  display: flex;
  width: 100%;
  align-items: center;
  justify-content: center;
  border-radius: 9999px;
  background: #FF8A00;
  padding: 13px 0;
  line-height: 22px;
  color: #FFFFFF;
  cursor: pointer;
}
```

**关注按钮**：
```css
.btn-follow {
  height: 36px;
  width: 82px;
  cursor: pointer;
  border-radius: 20.509px;
  border: 1px solid #FF8A00;
  background: #FFFFFF;
  font-size: 14px;
  line-height: 19px;
  font-weight: 500;
  color: #FF8A00;
  transition: color 0.15s, background-color 0.15s;
}
.btn-follow:hover {
  background: #FF8A00;
  color: #FFFFFF;
}
```

**侧栏导航按钮**：
```css
.nav-btn {
  display: flex;
  width: 100%;
  align-items: center;
  gap: 8px;
  border-radius: 9999px;
  padding: 13px 16px;
  font-size: 16px;
  line-height: 22px;
  color: #000000;
  transition: background-color 0.15s;
}
.nav-btn:hover {
  background-color: #F4F4F5;
}
.nav-btn.active {
  background-color: #F4F4F5;
}
```

**发现/关注切换按钮**：
```css
.tab-btn {
  display: flex;
  width: 86px;
  align-items: center;
  justify-content: center;
  gap: 10px;
  border-radius: 32px;
  padding: 9px 12px;
  font-size: 16px;
  text-align: center;
  transition: background-color 0.15s, color 0.15s;
}
.tab-btn.active {
  background: #F4F4F5;
  font-weight: 500;
  color: #292524;
}
.tab-btn.inactive {
  color: #44403C;
}
.tab-btn.inactive:hover {
  background: #F4F4F5;
  color: #292524;
}
```

**文章操作按钮（点赞/收藏/评论/分享）**：
```css
.action-btn {
  display: flex;
  width: fit-content;
  align-items: center;
  justify-content: center;
  gap: 4px;
  border-radius: 9999px;
  padding: 8px 12px;
  font-size: 14px;
  color: #525252;
  transition: background-color 0.15s;
  cursor: pointer;
}
.action-btn.like:hover   { background-color: #FFF7ED; }  /* orange-50 */
.action-btn.fav:hover    { background-color: #FFFBEB; }  /* amber-50 */
.action-btn.comment:hover { background-color: #EFF6FF; }  /* blue-50 */
.action-btn.share:hover  { background-color: #F0FDF4; }  /* green-50 */
```

### 头像组件

```css
.avatar {
  position: relative;
  overflow: hidden;
  border-radius: 9999px;
  border: 0.748px solid #F5F5F5;
  background: #FFFFFF;
  box-shadow: 0 0 10.67px 5.33px rgba(255, 232, 163, 0.80);
  width: 40px;
  height: 40px;
}
.avatar-inner {
  display: flex;
  width: 100%;
  height: 100%;
  align-items: center;
  justify-content: center;
  border-radius: 9999px;
  background: linear-gradient(to bottom right, #92D8C2, #F6D365);
  color: #FFFFFF;
  font-size: 15px;
}
```

### 导航组件

**顶部导航栏**：
```css
.top-header {
  position: fixed;
  top: 0;
  z-index: 30;
  width: 100%;
  border-bottom: 1px solid #F5F5F5;
  background: #FFFFFF;
  transition: transform 0.2s cubic-bezier(0, 0, 0.2, 1);
}
.header-inner {
  margin: 0 auto;
  display: flex;
  height: 72px;
  width: 100%;
  min-width: 0;
  align-items: center;
  justify-content: space-between;
  padding: 0 32px;
}
/* 移动端 */
@media (max-width: 768px) {
  .header-inner {
    height: 64px;
    gap: 16px;
    padding: 0 16px;
  }
}
```

**侧栏导航**：
```css
.sidebar {
  position: sticky;
  top: 73px;
  display: flex;
  flex-direction: column;
  background: #FFFFFF;
  padding-top: 20px;
  color: #000000;
  height: calc(100vh - 73px);
  width: 232px;
  transition: top 0.2s cubic-bezier(0, 0, 0.2, 1);
}
.sidebar-nav {
  flex: 1;
  overflow-y: auto;
  padding: 0 16px;
}
.sidebar-nav ul {
  space-y: 12px;
}
```

## 布局与间距

### 网格系统

- 侧栏布局：232px 固定侧栏 + 弹性内容区
- 内容区最大宽度：696px，居中显示
- 全局最大宽度：1440px（max-w-[1440px]）
- 采用 Flexbox 为主，无传统网格系统

### 断点设置

- 移动端：< 768px（max-md:）
- 桌面端：≥ 768px（md:）

### 间距系统

| 名称 | 值 | 应用场景 |
|------|-----|----------|
| xs | 8px | 组件内间距（头像与内容、按钮图标间距） |
| sm | 12px | 列表项间距、侧栏选项 |
| md | 16px | 标准间距、导航标签间距 |
| lg | 20-24px | 区块留白 |
| xl | 32px | 文章区块间距、容器水平内边距 |
| 2xl | 36px | 顶部导航链接间距 |

### 容器设置

```css
.container {
  margin: 0 auto;
  width: 100%;
  max-width: 1440px;
}
.content-area {
  margin: 0 auto;
  width: 100%;
  max-width: 696px;
}
.header-container {
  margin: 0 auto;
  display: flex;
  height: 72px;
  width: 100%;
  padding: 0 32px;
}
@media (max-width: 768px) {
  .header-container {
    height: 64px;
    padding: 0 16px;
  }
}
```

## 特效与交互

### 过渡效果

**默认过渡**：
```css
transition: color 0.15s cubic-bezier(0.4, 0, 0.2, 1),
            background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1),
            border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1);
```
- 缓动函数：`cubic-bezier(0.4, 0, 0.2, 1)`（ease-in-out）
- 时长：150ms，快节奏响应

**头部过渡**：
```css
transition: transform 0.2s cubic-bezier(0, 0, 0.2, 1);
```
- 缓动函数：ease-out
- 时长：200ms

### 悬停效果

- 导航按钮：背景变为 `#F4F4F5`（浅灰实色）
- 文章卡片：背景变为 `#F9FAFB`（极浅灰蓝）
- 关注按钮：背景变为 `#FF8A00`，文字变为 `#FFFFFF`（橙底白字反转）
- 操作按钮：分别变化为对应浅色背景（点赞→orange-50，收藏→amber-50，评论→blue-50，分享→green-50）
- 文章卡片内链接：文本颜色从 `#44403C` 变为 `#111827`

### 点击效果

- 侧栏导航按钮：按下态和点击后态背景均变为 `#F4F4F5`
- 文章卡片：按下态和点击后态背景均变为 `#F9FAFB`

### 动画效果

**脉搏加载动画**（图片占位）：
```css
@keyframes pulse {
  50% { opacity: 0.5; }
}
.animate-pulse {
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}
```

## 行业特色设计

### 科技/社交内容平台特有元素

**内容信息流布局**：
- 垂直滚动信息流，文章卡片依次排列
- 每篇文章包含：用户头像+名称、发布时间、关注按钮、内容媒体卡（图片+标题+摘要）、互动操作栏
- 无分页，无限滚动式加载

**行业组件**：
- 发现/关注双标签切换：内容筛选机制
- 跨类型操作按钮组（点赞/收藏/评论/分享）：每种操作有独立的悬停颜色
- 头像系统：渐变默认头像 + 发光阴影，提升社区感
- Beta 标签：灰底圆角标识产品阶段

**行业色彩规范**：
- 品牌色橙色在科技行业较为罕见，形成鲜明差异化
- 大量中性灰阶营造干净阅读环境
- 暖色系头像渐变注入人情味

**行业布局特点**：
- 三栏式布局（侧栏 + 内容流 + 右侧栏）
- 固定头部导航 + 固定侧栏导航
- 内容居中聚焦，最大宽度约束保证可读性

## 使用建议

### 适用场景

- 内容社区/社交平台
- 信息流类应用
- 创作者平台
- 科技类博客/资讯站
- Agent/协作工具类产品

### 避免场景

- 复杂数据表格/后台管理系统
- 传统企业官网
- 电商/产品展示为主
- 重表单类应用

### 最佳实践

1. 保持大面积留白，信息密度不宜过高
2. 橙色仅用于关键操作按钮，避免滥用
3. 圆角按钮带来亲和力，统一使用全圆角（rounded-full）
4. 过渡动画控制在 150ms-200ms，保持轻快感
5. 系统字体栈确保各平台表现一致

## CSS变量参考

```css
:root {
  /* 颜色 */
  --color-main: #FF8A00;
  --color-background: #FFFFFF;
  --color-foreground: #0F1419;
  --color-page-bg: #F5F5F5;
  --color-hover-bg: #F4F4F5;
  --color-card-hover: #F9FAFB;
  --color-text-primary: #0F1419;
  --color-text-secondary: #525252;
  --color-text-muted: #A1A1AA;
  --color-text-nav: #44403C;
  --color-text-username: #171717;
  --color-border-light: #F5F5F5;
  --color-card-border: rgb(239, 243, 244);
  --color-avatar-gradient-from: #92D8C2;
  --color-avatar-gradient-to: #F6D365;

  /* 间距 */
  --spacing-xs: 8px;
  --spacing-sm: 12px;
  --spacing-md: 16px;
  --spacing-lg: 20px;
  --spacing-xl: 24px;
  --spacing-2xl: 32px;

  /* 圆角 */
  --radius-sm: 4px;
  --radius-md: 12px;
  --radius-lg: 20.5px;
  --radius-full: 9999px;
  --radius-container: 32px;

  /* 阴影 */
  --shadow-avatar: 0 0 10.67px 5.33px rgba(255, 232, 163, 0.80);

  /* 过渡 */
  --transition-base: 0.15s cubic-bezier(0.4, 0, 0.2, 1);
  --transition-header: 0.2s cubic-bezier(0, 0, 0.2, 1);

  /* 字号 */
  --text-title: 17px;
  --text-body: 15px;
  --text-base: 16px;
  --text-sm: 14px;

  /* 字重 */
  --font-extrabold: 800;
  --font-medium: 500;
  --font-normal: 400;

  /* 容器 */
  --container-max: 1440px;
  --content-max: 696px;
  --sidebar-width: 232px;
  --header-height: 72px;
  --header-height-mobile: 64px;
}
```

## 设计原则总结

1. **轻盈克制**：大面积留白、低对比度灰阶背景，让内容成为视觉焦点
2. **橙色点睛**：品牌色仅用于关键交互触点（登录、关注），避免视觉疲劳
3. **圆角亲和**：全站 UI 组件统一圆角处理，从 4px（卡片）到 full（按钮），传递友好感
4. **细腻反馈**：150ms 过渡 + 浅色悬停背景，交互反馈即时但不突兀
5. **系统优先**：使用系统字体栈，跨平台零加载成本，确保性能与一致性

---

**最后更新时间**：2026-06-23
**版本**：1.0.0
**行业**：科技 / 社交内容平台
**来源**：https://zleap.com/
