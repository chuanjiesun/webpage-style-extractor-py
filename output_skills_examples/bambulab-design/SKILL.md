---
name: bambulab-design
description: 提取并应用 Bambu Lab 拓竹科技官网的设计风格与配色方案，适用于3D打印/制造科技行业网站页面设计。包含完整的色彩系统、排版规范、组件样式和布局指南。
meta:
  - "industry: 科技"
  - "category: 3D打印/制造科技"
---

# Bambu Lab 拓竹科技 设计风格指南

## 概述

Bambu Lab 拓竹科技官网采用深色+高对比度的现代科技风格设计，以品牌绿色 (#00AE42) 为核心视觉锚点，搭配深黑 (#1A1A1A) 和纯白 (#FFFFFF) 形成强烈视觉冲击。页面以大幅产品实景图为主视觉，配合简洁的文字和明确的CTA按钮，传达高端3D打印品牌的专业与科技感。整体设计克制而不失力度，大量留白与沉浸式大图展示结合，营造沉浸式产品体验。

**行业定位**：科技（3D打印/制造科技）
**设计风格**：现代、简约、高端科技感
**核心特点**：
1. 品牌绿 (#00AE42) 贯穿全局的视觉识别
2. 深色背景 + 大图沉浸式产品展示
3. 低圆角 (3-4px) 的功能性按钮设计
4. Manrope 字体家族带来的现代科技感
5. 黑白绿三色体系的高对比度视觉层次

## 色彩系统

### 主色调

**品牌主色**：`#00AE42` (RGB: 0, 174, 66)
- 用于：CTA按钮（商城、订阅）、新增标签（新品）、链接高亮
- 传达：创新、科技、环保、活力
- 行业特征：绿色在3D打印/制造科技行业中代表创新与可持续，区别于传统科技蓝

### 辅助色

**次要颜色**：
- `#1A1A1A` - 深黑色，用于主按钮背景、深色区块文字
- `#333333` - 深灰色，用于导航文字、浅色区块按钮文字
- `#F5F5F5` - 浅灰色，用于次要按钮背景、深色区块按钮文字
- `#9E9E9E` - 中灰色，用于辅助说明文字、语言切换按钮

### 文字颜色

**文本色系**：
- 标题（深色背景）：`#FFFFFF` - 白色标题
- 标题（浅色背景）：`#1A1A1A` - 深黑标题
- 导航文字：`#333333` - 深灰色导航项
- 正文：`#333333` - 深灰色正文
- 辅助文本：`#9E9E9E` - 中灰色辅助信息
- 链接/强调：`#00AE42` - 品牌绿色链接与高亮

### 强调色与功能色

**强调色**：
- CTA按钮：`#00AE42` (品牌绿)
- 新品标签（标准）：`#00AE42` (品牌绿)
- 新品标签（高端产品）：`#C6A169` (香槟金)
- 新品标签（特定产品）：`#FF6600` (活力橙)
- X2D 产品强调色：`#664beb` (科技紫) / `#938AFF` (浅紫)

**功能色**：
- 成功：`#00AE42`
- 错误：`#EF4444`
- 警告：`#F59E0B`
- 信息：`#333333`

### 渐变色

图片叠加渐变（从底部向上的黑色遮罩）：
```css
background: linear-gradient(0deg, rgb(0, 0, 0) 0%, rgba(0, 0, 0, 0) 100%);
```
用于产品卡片上的文字叠加层，确保白色文字在产品图片上清晰可读。

## 排版系统

### 字体家族

**主字体**：Manrope
- CSS: `font-family: Manrope, "Open Sans", "system-ui", "Segoe UI", Roboto, Oxygen, Ubuntu, "Fira Sans", "Droid Sans", "Helvetica Neue", sans-serif;`
- 后备字体：system-ui, Segoe UI, Roboto

**辅助字体**：Arial
- 用于：Cookie通知等第三方组件

### 字号层级

| 层级 | 字号 | 行高 | 字重 | 应用场景 |
|------|------|------|------|----------|
| Display | 100px | 110px | - | 超大展示标题（CSS变量定义） |
| Display-1-1 | 86px | 95px | - | 大展示标题（CSS变量定义） |
| Display-2 | 72px | 79px | - | 展示副标题（CSS变量定义） |
| Headline-1 | 60px | 66px | - | 主头条标题（CSS变量定义） |
| H2 (大) | 48px | 48.48px | 700 | 产品名称标题 |
| Headline-2 | 54px | 60px | - | 区块大标题（CSS变量定义） |
| Headline-3 | 48px | 53px | - | 区块标题（CSS变量定义） |
| Headline-4 | 40px | 48px | - | 小节标题（CSS变量定义） |
| H2 (中) | 30px | 36px | 700 | 副标题/区域标题 |
| Title-1 | 34px | 41px | - | 标题1（CSS变量定义） |
| Title-2 | 30px | 36px | - | 标题2（CSS变量定义） |
| Title-3 | 24px | 29px | - | 标题3（CSS变量定义） |
| H1 | 32px | 41.6px | 700 | 页面主标题 |
| H2 (小) | 22px | 36px | 600 | 小标题 |
| Body-1 | 18px | 24px | - | 大正文（CSS变量定义） |
| H2 (标签) | 16px | 22.4px | 700 | 分类标签标题 |
| Body-2 | 16px | 21px | - | 标准正文（CSS变量定义） |
| Button-1 | 16px | 22px | 400 | 按钮文字 |
| Body-3 | 14px | 20px | - | 辅助正文（CSS变量定义） |
| Body-4 | 14px | 20px | - | 紧凑正文（CSS变量定义） |
| Description-1 | 12px | 17px | - | 说明文字/小标注 |

### 字重与行高

**字重规范**：
- 粗体（700）：标题、产品名称、分类标签
- 半粗（600）：小标题
- 常规（400）：按钮、正文、导航

**行高规范**：
- 大标题：约 1.01（48px/48.48px）- 紧凑标题
- 中标题：约 1.2（30px/36px）
- 小标题：约 1.64（22px/36px）
- 正文：1.31-1.5
- 标签标题：1.4

## 组件样式

### 卡片组件

产品卡片采用无背景、无边框的极简设计，依赖产品图片本身作为视觉载体：
```css
.product-card {
  background: transparent;
  border: none;
  border-radius: 0px;
  box-shadow: none;
  padding: 0px;
}

.product-card .textContent {
  background: linear-gradient(0deg, rgb(0, 0, 0) 0%, rgba(0, 0, 0, 0) 100%);
}
```

### 按钮组件

**主按钮（购买/深色）**：
```css
.btn-primary-dark {
  background: #1A1A1A;
  color: #F5F5F5;
  border: none;
  border-radius: 4px;
  padding: 6px 16px;
  font-size: 16px;
  font-weight: 400;
  font-family: Manrope, "Open Sans", system-ui, sans-serif;
  cursor: pointer;
  transition: background-color 0.25s cubic-bezier(0.4, 0, 0.2, 1),
              box-shadow 0.25s cubic-bezier(0.4, 0, 0.2, 1),
              border-color 0.25s cubic-bezier(0.4, 0, 0.2, 1),
              color 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}

.btn-primary-dark:hover {
  box-shadow: 0 5px 5px -3px rgba(145,158,171,0.2),
              0 8px 10px 1px rgba(145,158,171,0.14),
              0 3px 14px 2px rgba(145,158,171,0.12);
}

.btn-primary-dark:active {
  box-shadow: 0 5px 5px -3px rgba(145,158,171,0.2),
              0 8px 10px 1px rgba(145,158,171,0.14),
              0 3px 14px 2px rgba(145,158,171,0.12);
}
```

**次要按钮（了解更多/深色背景）**：
```css
.btn-secondary-transparent {
  background: transparent;
  color: #1A1A1A;
  border: none;
  border-radius: 4px;
  padding: 6px 16px;
  font-size: 16px;
  font-weight: 400;
  cursor: pointer;
}

.btn-secondary-transparent:hover {
  background: rgba(51, 51, 51, 0.08);
}
```

**次要按钮（浅色背景）**：
```css
.btn-secondary-light {
  background: #F5F5F5;
  color: #333333;
  border: none;
  border-radius: 4px;
  padding: 6px 16px;
  font-size: 16px;
  font-weight: 400;
  cursor: pointer;
}
```

**CTA按钮（商城/品牌绿）**：
```css
.btn-cta-green {
  background: #00AE42;
  color: #FFFFFF;
  border: none;
  border-radius: 3px;
  padding: 4px 12px;
  font-size: 16px;
  font-weight: 400;
  cursor: pointer;
  transition: background-color 0.25s cubic-bezier(0.4, 0, 0.2, 1),
              box-shadow 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}

.btn-cta-green:hover {
  background: #008733;
}

.btn-cta-green:active {
  box-shadow: 0 5px 5px -3px rgba(145,158,171,0.2),
              0 8px 10px 1px rgba(145,158,171,0.14),
              0 3px 14px 2px rgba(145,158,171,0.12);
}
```

**订阅按钮**：
```css
.btn-subscribe {
  background: #00AE42;
  color: #FFFFFF;
  border: none;
  border-radius: 0px 3px 3px 0px;
  padding: 6px 16px;
  font-size: 16px;
  font-weight: 400;
  cursor: pointer;
}

.btn-subscribe:hover {
  background: #007B55;
  box-shadow: 0 2px 4px -1px rgba(145,158,171,0.2),
              0 4px 5px 0px rgba(145,158,171,0.14),
              0 1px 10px 0px rgba(145,158,171,0.12);
}
```

### 表单组件

**文本输入框**：
```css
.input-text {
  background: #F5F5F5;
  border: none;
  border-radius: 0px;
  padding: 6px 16px;
  font-size: 16px;
  color: #333333;
  font-family: Manrope, "Open Sans", system-ui, sans-serif;
}
```

**复选框**：
```css
.input-checkbox {
  background: transparent;
  border: none;
}
```

### 导航组件

**顶部导航栏**：
```css
.navbar {
  position: fixed;
  top: 0;
  height: 56px;
  background: rgba(0, 0, 0, 0);
  z-index: 1000;
}

.nav-item {
  color: #333333;
  font-size: 16px;
  font-weight: 400;
  transition: background-color 0.25s;
}

.nav-item:hover {
  background: rgba(51, 51, 51, 0.08);
}
```

### 标签组件

**新品标签（品牌绿）**：
```css
.badge-new {
  color: #00AE42;
  font-size: 12px;
  line-height: 17px;
  font-weight: 400;
}
```

**新品标签（香槟金）**：
```css
.badge-new-premium {
  color: #C6A169;
  font-size: 12px;
  line-height: 17px;
}
```

**新品标签（活力橙）**：
```css
.badge-new-orange {
  color: #FF6600;
  font-size: 12px;
  line-height: 17px;
}
```

## 布局与间距

### 网格系统

**产品展示网格**：
- 3列等宽布局，每列 384px，间距 16px
- 总宽 1168px (3 × 384 + 2 × 16)

**全宽容器**：
- 宽度 1920px（固定视口宽度）
- 无最大宽度约束

### 断点设置

**视口基准**：1920 × 1080（桌面端优先设计）
- 移动端：< 768px
- 平板端：768px - 1023px
- 桌面端：≥ 1024px
- 大屏：≥ 1920px

### 间距系统

**Section 间距（区块间距）**：

| 名称 | 值 | 应用场景 |
|------|-----|----------|
| Section-Gap-1 | 60px | 小区块间距 |
| Section-Gap-2 | 80px | 标准区块间距 |
| Section-Gap-3 | 100px | 中等区块间距 |
| Section-Gap-4 | 140px | 大区块间距 |
| Section-Gap-5 | 160px | 较大区块间距 |
| Section-Gap-6 | 200px | 大区块间距 |
| Section-Gap-7 | 240px | 超大区块间距 |
| Section-Gap-8 | 320px | 最大区块间距 |

**Content 间距（内容间距）**：

| 名称 | 值 | 应用场景 |
|------|-----|----------|
| Content-Gap-1 | 4px | 极紧凑间距 |
| Content-Gap-2 | 8px | 紧凑间距 |
| Content-Gap-2-1 | 10px | 按钮内小间距 |
| Content-Gap-3 | 12px | 小间距 |
| Content-Gap-4 | 16px | 标准间距 |
| Content-Gap-5 | 18px | 中小间距 |
| Content-Gap-6 | 20px | 中间距 |
| Content-Gap-7 | 24px | 大间距 |
| Content-Gap-8 | 32px | 较大间距 |
| Content-Gap-9 | 40px | 大间距 |
| Content-Gap-10 | 48px | 超大间距 |

**Button 间距**：

| 名称 | 值 | 应用场景 |
|------|-----|----------|
| Button-Gap-1 | 10px | 按钮内间距 |
| Button-Gap-2 | 20px | 按钮组间距 |

**Gutter 间距**：

| 名称 | 值 | 应用场景 |
|------|-----|----------|
| Gutter-Gap-1 | 24px | 标准侧边间距 |
| Gutter-Gap-2 | 100px | 大侧边间距 |

### 容器设置

```css
.container {
  width: 1920px;
  margin: 0 auto;
  padding: 0;
}
```

## 特效与交互

### 过渡效果

```css
/* 按钮过渡（最常用） */
transition: background-color 0.25s cubic-bezier(0.4, 0, 0.2, 1),
            box-shadow 0.25s cubic-bezier(0.4, 0, 0.2, 1),
            border-color 0.25s cubic-bezier(0.4, 0, 0.2, 1),
            color 0.25s cubic-bezier(0.4, 0, 0.2, 1);

/* 变换过渡 */
transition: transform 0.5s ease-in-out;

/* 快速过渡 */
transition: transform 0.225s cubic-bezier(0.4, 0, 0.2, 1);

/* 透明度过渡 */
transition: opacity 0.3s ease;

/* 间距过渡 */
transition: margin 0.15s cubic-bezier(0.4, 0, 0.2, 1);
```

### 悬停效果

- CTA按钮（商城）：背景色从 `#00AE42` 变为 `#008733`（加深绿色）
- 订阅按钮：背景色变为 `#007B55`，添加阴影
- 导航项：背景色变为 `rgba(51, 51, 51, 0.08)`（浅灰高亮）
- 产品按钮：添加 MUI 标准阴影

### 点击效果

- 按钮：阴影加深（active 状态下阴影更大更深）
  ```css
  box-shadow: 0 5px 5px -3px rgba(145,158,171,0.2),
              0 8px 10px 1px rgba(145,158,171,0.14),
              0 3px 14px 2px rgba(145,158,171,0.12);
  ```

### 动画效果

**加载旋转动画**：
```css
/* 圆形进度条旋转 */
@keyframes animation-61bdi0 {
  animation-duration: 1.4s;
  animation-timing-function: linear;
  animation-iteration-count: infinite;
}

/* 圆形进度描边 */
@keyframes animation-1p2h4ri {
  animation-duration: 1.4s;
  animation-timing-function: ease-in-out;
  animation-iteration-count: infinite;
}
```

## 行业特色设计

### 科技/3D打印行业特有元素

**产品展示模式**：
- 全屏沉浸式产品大图：每个产品占据完整视口高度的大图展示区
- 产品名称 + 简短描述 + 双按钮（了解更多 / 立即购买）的标准展示结构
- 产品网格：3列等宽产品卡片，依赖产品图片而非卡片边框/阴影

**品牌色彩规范**：
- 绿色 (#00AE42) 作为核心品牌识别色，贯穿全站CTA元素
- 深色系 (#1A1A1A, #000000) 营造专业科技感
- 多彩新品标签区分产品线：绿色、香槟金、活力橙、科技紫

**行业组件**：
- 产品规格标签（新品/热销）
- 产品类别导航（3D打印机 / 耗材 / 配件 / 软件 / MakerWorld）
- 订阅入口
- 新闻资讯卡片
- 地区/语言切换器

**行业布局特点**：
- 纵向滚动的沉浸式产品展示
- 全屏轮播首屏
- 固定顶部导航栏 (56px)
- 产品按类别分区展示

## 使用建议

### 适用场景

- ✅ 3D打印/制造科技产品官网
- ✅ 高端科技产品展示页面
- ✅ 以产品大图为核心的电商平台
- ✅ 品牌绿为主色调的科技品牌设计
- ✅ 沉浸式滚动产品展示页面

### 避免场景

- ❌ 信息密集型后台管理系统
- ❌ 大量文字内容的博客/资讯网站
- ❌ 儿童/教育类网站
- ❌ 传统企业展示网站

### 最佳实践

1. 保持大图展示区的视觉冲击力，避免过多文字叠加
2. 品牌绿 (#00AE42) 仅用于CTA关键操作，不宜大面积使用
3. 按钮圆角保持在 3-4px，与整体硬朗风格一致
4. 利用 linear-gradient 黑色遮罩确保浅色文字在图片上的可读性
5. 内容间距严格遵循 CSS 变量定义的间距系统

## CSS变量参考

```css
:root {
  /* 品牌色 */
  --color-primary: #00AE42;
  --color-primary-hover: #008733;
  --color-primary-active: #007B55;
  --color-dark: #1A1A1A;
  --color-text-primary: #333333;
  --color-text-secondary: #9E9E9E;
  --color-bg-light: #F5F5F5;
  --color-bg-white: #FFFFFF;
  --color-accent-gold: #C6A169;
  --color-accent-orange: #FF6600;
  --color-accent-purple: #664beb;
  --color-accent-purple-light: #938AFF;
  --color-icon: #333333;
  --color-icon-fill: #F5F5F5;

  /* Section间距 */
  --spacing-section-1: 60px;
  --spacing-section-2: 80px;
  --spacing-section-3: 100px;
  --spacing-section-4: 140px;
  --spacing-section-5: 160px;
  --spacing-section-6: 200px;
  --spacing-section-7: 240px;
  --spacing-section-8: 320px;

  /* Content间距 */
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  --spacing-xl: 32px;
  --spacing-2xl: 48px;

  /* 按钮间距 */
  --spacing-button-sm: 10px;
  --spacing-button-md: 20px;

  /* 圆角 */
  --radius-sm: 3px;
  --radius-md: 4px;

  /* 导航 */
  --navbar-height: 56px;

  /* 字体 */
  --font-family: Manrope, "Open Sans", "system-ui", "Segoe UI", Roboto, Oxygen, Ubuntu, "Fira Sans", "Droid Sans", "Helvetica Neue", sans-serif;

  /* 排版 */
  --font-h1: 32px;
  --font-h2-lg: 48px;
  --font-h2-md: 30px;
  --font-h2-sm: 22px;
  --font-h2-label: 16px;
  --font-body: 16px;
  --font-small: 14px;
  --font-desc: 12px;

  /* 过渡 */
  --transition-base: 0.25s cubic-bezier(0.4, 0, 0.2, 1);
  --transition-fast: 0.15s cubic-bezier(0.4, 0, 0.2, 1);
  --transition-slow: 0.5s ease-in-out;

  /* 阴影 */
  --shadow-btn-hover: 0 2px 4px -1px rgba(145,158,171,0.2),
                      0 4px 5px 0px rgba(145,158,171,0.14),
                      0 1px 10px 0px rgba(145,158,171,0.12);
  --shadow-btn-active: 0 5px 5px -3px rgba(145,158,171,0.2),
                       0 8px 10px 1px rgba(145,158,171,0.14),
                       0 3px 14px 2px rgba(145,158,171,0.12);
}
```

## 设计原则总结

1. **沉浸式视觉优先**：产品大图占满视口，让产品本身成为视觉焦点，减少装饰性元素干扰
2. **品牌绿点睛**：品牌绿 #00AE42 仅用于关键CTA和状态标识，保持克制以维持视觉冲击力
3. **极简功能主义**：低圆角(3-4px)、无边框卡片、无阴影产品设计，以功能驱动视觉
4. **高对比度阅读**：深色背景配白色文字、浅色背景配深灰文字，确保所有场景下文字清晰可读
5. **系统化间距**：严格的间距变量系统（Section/Content/Button/Gutter 四级）保证页面节奏一致性

---

**最后更新时间**：2026-04-16
**版本**：1.0.0
**行业**：科技（3D打印/制造科技）
