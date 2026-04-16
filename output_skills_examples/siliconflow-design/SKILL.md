---
name: siliconflow-design
description: 提取并应用硅基流动 SiliconFlow 的设计风格与配色方案，适用于AI基础设施/云计算科技行业网站页面设计。包含完整的紫色品牌色彩系统、中英文字体排版规范、卡片组件样式和布局指南。
meta:
  - "industry: tech"
  - "category: ai-infrastructure"
---

# 硅基流动 SiliconFlow 设计风格指南

## 概述

硅基流动（SiliconFlow）是面向 AI 基础设施的云端服务平台，致力于成为全球领先的 AI 能力提供商。页面设计采用现代科技风格，以鲜明的品牌紫色为核心，搭配深色渐变区块与白色内容区域形成视觉层次。排版简洁大气，数据指标以超大字号展示，传达技术实力与专业感。

**行业定位**：科技 / AI 基础设施
**设计风格**：现代、科技感、简约
**核心特点**：
- 品牌紫色（#6E29F6）贯穿全局
- 深色渐变与白色区块交替布局
- 超大数据指标展示（84px/72px 粗体）
- Tailwind CSS 驱动的精细化间距
- 紫色系交互反馈（hover/active 均变为品牌紫）

## 色彩系统

### 主色调

**品牌主色**：`#6E29F6` (RGB: 110, 41, 246 | HSL: 260, 92%, 56%)
- CSS变量：`--primary: 260,92%,56%`
- 用于：品牌标识、CTA 按钮、交互悬停态、渐变终点色
- 传达：创新、科技、智能
- 行业特征：典型的 AI/科技行业紫色，区别于传统蓝色

### 辅助色

**次要颜色**：
- `#743AED` - 深紫，用于渐变中段、强调元素过渡
- `#5922C6` - 暗紫，用于深色区域品牌色延伸
- `#9E70F9` - 浅紫，用于边框装饰、分隔线
- `#844BF7` - 亮紫，用于渐变与图标高亮

### 文字颜色

**文本色系**：
- 标题：`#1E293B` (slate-800) - 主要标题文字，深色内容区
- 正文：`#475569` (slate-600) - 段落文本、列表项
- 辅助文本：`#64748B` (slate-500) - 次要说明文字
- 深色区块标题：`#FAFDFF` - 白色微蓝，用于深色背景上标题
- 深色区块正文：`#FFFFFF` - 纯白，用于深色/渐变背景上文字
- 链接默认：`#1E293B` - 与正文同色
- 链接悬停：`#6E29F6` - 品牌紫色

### 强调色与功能色

**强调色**：
- CTA/登录按钮背景：`#6E29F6` 品牌紫
- 模型分类标签色：
  - 语言：`#156D3B` 绿色
  - 语音：`#5922C6` 紫色
  - 图片：`#475569` 灰蓝
  - 视频：`#006692` 蓝色

**功能色**：
- 成功：`#156D3B`
- 错误：`#EF4444`
- 警告：`#F59E0B`
- 信息：`#6E29F6`

### 渐变色

**品牌渐变**（核心渐变，多次用于 Hero 区与产品展示区）：
```css
background: linear-gradient(to right, #252736, #6E29F6);
```
- 方向：从左到右
- 起点色：`#252736`（深蓝灰）
- 终点色：`#6E29F6`（品牌紫）

### 深色区块背景色

- `#1D1F2C` - 最深背景，用于速度/性能数据展示区
- `#252736` - 深色背景，渐变起点
- `#36384A` - 中深色背景
- 紫色边框分隔：`#9E70F9` - 深色区块内的分隔线

### 浅色区块背景色

- `#FFFFFF` - 主内容区白色背景
- `#F5F5F8` - 卡片背景、特性展示区
- `#FAFDFF` - 浅蓝白背景
- `#F1F1FF` - 淡紫色背景
- `#F1FFF9` - 淡绿色背景
- `#E3E3E3` - 边框灰色

## 排版系统

### 字体家族

**主字体**：Roboto
- CSS: `font-family: Roboto, "SF Pro SC", "SF Pro Display", "SF Pro Icons", "PingFang SC", BlinkMacSystemFont, -apple-system, "Segoe UI", "Microsoft Yahei", Ubuntu, Cantarell, "Fira Sans", "Droid Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;`
- 后备字体：PingFang SC (macOS中文)、Microsoft Yahei (Windows中文)

**辅助字体**（Ant Design 组件）：
- CSS: `font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";`
- 用于：轮播、弹窗等 Ant Design 组件

### 字号层级

| 层级 | 字号 | 行高 | 字重 | 应用场景 |
|------|------|------|------|----------|
| Hero 标题 | 72px | 140px | 600 | 客户合作伙伴区大标题 |
| 大数据指标 | 84px | 100% | 700 | 性能数据展示（10x+、66%、1s等） |
| 移动端大数据 | 64px | 100% | 700 | 移动端性能数据 |
| 页面主标题 | 48px | 72px | 700 | 各区块主标题 |
| 行业标签大字 | 40px | 60px | 600 | 行业方案选中态标题 |
| 行业标签小字 | 40px | 40px | 600 | 行业方案选中态标题(移动) |
| 区块标题 | 36px | 36px | 600 | 特性标题（高速推理/高性价比） |
| 区块副标题 | 32px | 48px | 600 | 产品介绍标题 |
| 卡片标题 | 24px | 36px | 600 | 行业标签/功能分类标题 |
| 数据说明文字 | 24px | 100% | 400 | 性能指标说明文字 |
| 移动端标题 | 38px | - | 700 | 移动端区块主标题 |
| 正文 | 16px | 28px | 400 | 段落文本、列表项 |
| 辅助信息 | 16px | 24px | 400 | 页脚链接、版权信息 |

### 字重与行高

**字重规范**：
- 粗体（700）：大数据指标、页面主标题
- 半粗（600）：区块标题、标签标题、行业标题
- 常规（400）：正文、描述、辅助文本

**行高规范**：
- 超大标题：1.94（140px/72px）
- 大标题：1.5（72px/48px）
- 中标题：1.5（48px/32px）
- 小标题：1.5（36px/24px）
- 正文：1.75（28px/16px）
- 紧凑文本：1.5（24px/16px）

## 组件样式

### 卡片组件

**特性展示卡片**（高稳定性/高智能/高安全性/高扩展性）：
```css
.feature-card {
  background: #F5F5F8;
  padding: 32px 32px 48px;
  max-width: 326px;
  min-height: 520px;
}

.feature-card h3 {
  font-size: 32px;
  font-weight: 600;
  color: #1E293B;
  text-align: center;
  margin-bottom: 40px;
}

.feature-card li {
  color: #475569;
  font-size: 16px;
  line-height: 28px;
}
```

**行业方案选中卡片**：
```css
.industry-card-active {
  height: 406px;
  border-radius: 8px;
  padding: 30px 25px;
  color: #FFFFFF;
  cursor: default;
  overflow: hidden;
}

.industry-card-active h3 {
  font-size: 40px;
  font-weight: 600;
  margin-bottom: 20px;
  color: #FFFFFF;
}

.industry-card-active p {
  font-size: 16px;
  color: #FFFFFF;
}
```

**行业方案未选中卡片**：
```css
.industry-card-default {
  height: 406px;
  cursor: default;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #FFFFFF;
}

.industry-card-default h3 {
  font-size: 24px;
  font-weight: 600;
  text-align: center;
  padding: 0 26px;
  color: #FFFFFF;
}
```

**性能数据卡片**（深色渐变背景）：
```css
.performance-card {
  background: #1D1F2C;
  color: #FAFDFF;
  padding-left: 92px;
  border-bottom: 1px solid #9E70F9;
}

.performance-card .big-number {
  font-size: 84px;
  font-weight: 700;
  line-height: 100%;
  margin-bottom: 12px;
}

.performance-card .label {
  font-size: 24px;
  line-height: 100%;
}
```

**高性价比卡片**（浅色背景）：
```css
.cost-card {
  max-width: 584px;
  border-radius: 15px;
  background: #FAFDFF;
  border: 1px solid #DEDFEE;
  color: #000000;
}
```

### 按钮组件

**登录按钮 / CTA 按钮**：
```css
.btn-login {
  background: #6E29F6;
  color: #FFFFFF;
  font-weight: 500;
  transition: all 0.15s cubic-bezier(0.4, 0, 0.2, 1);
}

.btn-login:hover {
  background: #5922C6;
}
```

**导航链接按钮**：
```css
.nav-link {
  color: #1E293B;
  font-size: 16px;
  transition: color 0.15s cubic-bezier(0.4, 0, 0.2, 1);
  text-decoration: none;
}

.nav-link:hover {
  color: #6E29F6;
}
```

### 导航组件

**顶部导航栏**：
```css
.navbar {
  position: sticky;
  top: 0;
  z-index: 50;
  background: #FFFFFF;
  padding: 16px 32px;
  height: 78px;
  transition: all 0.3s;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.navbar-nav {
  display: flex;
  align-items: center;
  gap: 36px;
  padding-left: 80px;
}
```

### 轮播组件（Ant Design）

```css
.ant-carousel .slick-dots li button {
  opacity: 0.2;
  background: #FFFFFF;
}

.ant-carousel .slick-dots li button:hover {
  opacity: 0.75;
}

.ant-carousel .slick-dots li.slick-active button {
  opacity: 1;
  color: rgba(0, 0, 0, 0.88);
}

.ant-carousel .slick-list:focus {
  outline: none;
}
```

## 布局与间距

### 网格系统

**特性卡片网格**（桌面端）：
```css
.features-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
}
```

**移动端**：
```css
@media (max-width: 768px) {
  .features-grid {
    grid-template-columns: 1fr;
  }
}
```

### 断点设置

- 移动端：< 768px（`when-mobile-screen` 自定义类）
- 桌面端：≥ 768px
- 站点基于 Tailwind CSS，使用 `when-mobile-screen` 作为移动端断点前缀

### 间距系统

| 名称 | 值 | 应用场景 |
|------|-----|----------|
| xs | 4px | 图标与文字间距（gap-[4px]） |
| sm | 12px | 大数据指标下间距（mb-[12px]） |
| md | 16px | 列表项间距（space-y-[16px]）、导航栏内边距 |
| lg | 20px | 卡片网格间距（gap-[20px]）、区块水平内边距（px-[20px]） |
| xl | 32px | 卡片内边距（px-[32px]）、导航栏水平内边距 |
| 2xl | 40px | 行业方案内边距（px-[40px]） |
| 3xl | 48px | 卡片垂直内边距（py-[48px]） |
| 4xl | 66px | 区块标题下方间距（mb-[66px]） |
| 5xl | 74px | 区块之间间距（mb-[74px]） |
| 6xl | 92px | 性能数据区左侧内边距（pl-[92px]）、标题下方间距（mb-[92px]） |
| 7xl | 110px | 底部区块下内边距（pb-[110px]） |

### 容器设置

```css
.container {
  max-width: 1265px;
  margin: 0 auto;
}
```

## 特效与交互

### 过渡效果

```css
/* 导航链接 & 按钮颜色过渡 */
transition: color 0.15s cubic-bezier(0.4, 0, 0.2, 1),
            background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1),
            border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1),
            text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1),
            fill 0.15s cubic-bezier(0.4, 0, 0.2, 1),
            stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1);

/* 变换过渡 */
transition: transform 0.15s cubic-bezier(0.4, 0, 0.2, 1);

/* 透明度过渡 - 慢速 */
transition: opacity 0.5s cubic-bezier(0.4, 0, 0.2, 1);

/* 透明度过渡 - 中速 */
transition: opacity 0.7s cubic-bezier(0.4, 0, 0.2, 1);

/* 通用过渡 */
transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);

/* 快速透明度 */
transition: opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1);
```

### 悬停效果

- 导航链接：颜色从 `#1E293B` 变为 `#6E29F6`（品牌紫）
- 轮播指示器：透明度从 0.2 增至 0.75
- 活跃指示器悬停：透明度保持 1

### 点击效果

- 导航链接：颜色从 `#1E293B` 变为 `#6E29F6`（与悬停相同）
- 按下态与点击后态颜色变化一致

### 焦点效果

- 轮播容器焦点：`outline: none`

## 行业特色设计

### AI 基础设施行业特有元素

**行业色彩规范**：
- 品牌紫色作为主色调，区别于传统 SaaS 蓝色
- 深色渐变区块象征技术深度与算力
- 多色分类标签（绿/紫/灰/蓝）区分模型类型

**行业组件**：
- 性能数据展示区：超大字号（84px）+ 渐变背景，展示推理速度/成本优势
- 模型分类标签：语言(绿)、语音(紫)、图片(灰)、视频(蓝)
- 行业方案轮播：卡片式切换，选中态展开详情
- 客户 Logo 墙：合作伙伴展示

**行业布局特点**：
- Hero 区使用深色渐变背景，立即传达科技感
- 产品介绍采用白底 + 卡片交替布局
- 数据指标区用大数字+深色背景形成强视觉冲击
- 行业方案区使用水平 Tab + 详情面板布局

## 使用建议

### 适用场景

- ✅ AI/ML SaaS 平台官网
- ✅ 云计算基础设施产品页
- ✅ API 服务商落地页
- ✅ 科技公司品牌站
- ✅ 数据密集型产品展示页

### 避免场景

- ❌ 传统企业官网（紫色过于科技感）
- ❌ 儿童教育类网站（色调偏冷暗）
- ❌ 奢侈品牌网站（缺少精致感）

### 最佳实践

1. 保持品牌紫色 `#6E29F6` 作为唯一的强调色，避免引入竞争色彩
2. 深色渐变区块与白色区块交替使用，形成视觉节奏
3. 大数据指标使用 84px/700 字重，辅以 24px 说明文字
4. 中英文混排时，确保 PingFang SC / Microsoft Yahei 回退字体可用
5. 所有交互过渡使用 `cubic-bezier(0.4, 0, 0.2, 1)` 缓动函数

## CSS变量参考

```css
:root {
  /* 品牌色 */
  --color-primary: #6E29F6;
  --color-primary-dark: #5922C6;
  --color-primary-light: #9E70F9;
  --color-primary-hsl: 260, 92%, 56%;

  /* 文字颜色 */
  --color-text-heading: #1E293B;
  --color-text-body: #475569;
  --color-text-secondary: #64748B;
  --color-text-on-dark: #FAFDFF;
  --color-text-on-dark-body: #FFFFFF;

  /* 背景颜色 */
  --bg-white: #FFFFFF;
  --bg-card: #F5F5F8;
  --bg-blue-white: #FAFDFF;
  --bg-light-purple: #F1F1FF;
  --bg-light-green: #F1FFF9;
  --bg-dark-1: #1D1F2C;
  --bg-dark-2: #252736;
  --bg-dark-3: #36384A;

  /* 边框颜色 */
  --border-default: #E5E7EB;
  --border-purple: #9E70F9;
  --border-light: #DEDFEE;

  /* 间距 */
  --spacing-xs: 4px;
  --spacing-sm: 12px;
  --spacing-md: 16px;
  --spacing-lg: 20px;
  --spacing-xl: 32px;
  --spacing-2xl: 40px;
  --spacing-3xl: 48px;
  --spacing-4xl: 66px;
  --spacing-5xl: 74px;
  --spacing-6xl: 92px;
  --spacing-7xl: 110px;

  /* 圆角 */
  --radius-sm: 8px;
  --radius-md: 15px;

  /* 过渡 */
  --transition-fast: 0.15s cubic-bezier(0.4, 0, 0.2, 1);
  --transition-normal: 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  --transition-slow: 0.5s cubic-bezier(0.4, 0, 0.2, 1);
  --transition-slower: 0.7s cubic-bezier(0.4, 0, 0.2, 1);

  /* 渐变 */
  --gradient-brand: linear-gradient(to right, #252736, #6E29F6);

  /* 阴影 */
  --shadow-none: none;
}
```

## 设计原则总结

1. **品牌一致性**：紫色（#6E29F6）贯穿全站，从导航悬停到 CTA 按钮到渐变终点，构建强烈的品牌识别
2. **数据驱动展示**：使用超大字号（84px/72px）展示关键性能指标，用数字说话
3. **深浅交替节奏**：深色渐变区块与白色内容区交替出现，避免视觉疲劳
4. **克制交互**：过渡效果简洁统一（0.15s/0.3s），颜色变化为主，不使用复杂动画
5. **中英兼容**：字体栈覆盖 macOS/Windows/Linux/Android 中文字体，确保中英文混排效果

---

**最后更新时间**：2026-04-16
**版本**：1.0.0
**行业**：科技 / AI 基础设施
