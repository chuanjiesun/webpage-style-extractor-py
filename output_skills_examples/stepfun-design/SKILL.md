---
name: stepfun-design
description: 提取并应用阶跃星辰 StepFun 的设计风格与配色方案，适用于AI对话/科技行业网站页面设计。包含暖灰色品牌色系、Gilroy字体排版规范、对话界面组件和侧边栏布局指南。
meta:
  - "industry: tech"
  - "category: ai-chat"
---

# 阶跃星辰 StepFun 设计风格指南

## 概述

阶跃星辰（StepFun）是一个 AI 对话产品平台，页面设计以暖灰棕色（#2A2424）为核心品牌色，搭配奶油白/暖纸质底色，营造克制而高级的阅读型对话体验。风格受到纸本书写质感启发，拒绝科技蓝/紫的刻板印象，用暖灰+金色调传达"思考与创作"的品牌气质。页面为经典的三栏对话布局：左侧会话列表、中间对话区、右侧功能面板。

**行业定位**：科技 / AI 对话
**设计风格**：现代、克制、书卷气
**核心特点**：
- 暖灰棕色（#2A2424）品牌色 + 金色调底色（#FCFCF9）
- Gilroy 几何无衬线字体，传达国际感与现代感
- 精细的透明度层级系统（rgba(42,36,36, 0.04~0.8)）
- 圆形操作按钮（border-radius: 9999px）+ 圆角方形内容按钮
- 多彩功能标签系统（蓝/绿/橙/紫/红/金）

## 色彩系统

### 主色调

**品牌主色（Content Primary）**：`#2A2424` (RGB: 42, 36, 36)
- CSS变量：`--content-primary: rgba(42,36,36,1)` / `--primary: 240 5.9% 10%`
- 用于：标题、按钮文字、图标、强调文字
- 传达：稳重、专业、内敛
- 行业特征：暖棕色而非纯黑，与纸质底色形成温暖对比，区别于冷黑+白的标准科技配色

### 辅助色

**多色功能系统**（CSS变量已定义完整色彩体系）：

- `#3986C5` - 功能蓝，用于信息类标签、Web Search
- `#74AD5D` - 功能绿，用于成功状态、Diligence Check
- `#E5893E` - 功能橙，用于警示状态、Image Creation
- `#8361B0` - 功能紫，用于知识库、Knowledge Base
- `#D55959` - 功能红，用于错误状态、危险操作
- `#806E59` - 金色文字，用于金色填充标签

### 文字颜色

**文本色系**（基于 #2A2424 的透明度层级）：
- 主文字：`#2A2424` (`--content-primary`) - 标题、重要文字
- 次要文字：`rgba(42, 36, 36, 0.7)` (`--content-secondary`) - 副标题、说明文字
- 辅助文字：`rgba(42, 36, 36, 0.5)` (`--content-tertiary`) - 标签、提示
- 禁用文字：`rgba(42, 36, 36, 0.35)` (`--content-disable`) - 不可用状态
- 悬停文字：`rgba(42, 36, 36, 0.8)` (`--content-hover`) - 悬停态强化
- 反色文字：`#FFFFFF` (`--content-reverse`) - 深色背景上的文字
- 极淡文字：`#BBBBBB` (`--content-quaterary`) - 极弱辅助信息

### 强调色与功能色

**功能色完整体系**：

| 功能色 | 主色 | 悬停 | 按下 | 边框 | 填充 |
|--------|------|------|------|------|------|
| 蓝 Blue | #3986C5 | rgba(57,134,197,0.7) | #2C6899 | rgba(57,134,197,0.5) | rgba(57,134,197,0.1) |
| 绿 Green | #74AD5D | rgba(116,173,93,0.7) | #5C8A4A | rgba(116,173,93,0.5) | rgba(116,173,93,0.1) |
| 橙 Orange | #E5893E | rgba(229,137,62,0.7) | #C26921 | rgba(229,137,62,0.5) | rgba(229,137,62,0.1) |
| 紫 Purple | #8361B0 | rgba(131,97,176,0.7) | #6E52B0 | rgba(131,97,176,0.5) | rgba(131,97,176,0.1) |
| 红 Red | #D55959 | rgba(213,89,89,0.7) | #B24B4B | rgba(213,89,89,0.5) | rgba(213,89,89,0.1) |
| 金 Gold | - | - | rgba(128,110,89,0.3) | rgba(128,110,89,0.5) | rgba(128,110,89,0.1) |

### 渐变色

**消息列表渐隐遮罩**：
```css
background: linear-gradient(0deg, #FCFCF9, rgba(252, 252, 249, 0));
```
- 用于：对话消息列表底部，实现滚动内容渐隐效果

### 背景色调

- `#FCFCF9` - 主底色（Paper 奶油白），CSS变量 `--background`
- `#F6F4F1` - 金底色（Gold BG），CSS变量 `--bg-gold`
- `#FAF9F5` - 浅金底色（Shallow Gold），CSS变量 `--color-fill-shallowgold`
- `#F3F1EE` - 悬停底色（Hover New），CSS变量 `--hover-new`
- `#FFFFFF` - 卡片/弹出层白色，CSS变量 `--color-fill-white`
- `rgba(42, 36, 36, 0.04)` - 极淡填充（Fill Gray），CSS变量 `--color-fill-gray`
- `rgba(202, 197, 190, 0.1)` - 悬停背景（Hover），CSS变量 `--hover`

### 悬停背景色

- `rgba(202, 197, 190, 0.1)` - 通用悬停背景（`--hover`）
- `rgba(128, 110, 89, 0.08)` - 二级悬停背景（`--hover-hover`）
- `#F3F1EE` - 实色悬停背景（`--hover-new`）
- `rgba(202, 197, 190, 0.16)` - 强悬停背景

### 边框颜色

- `rgba(42, 36, 36, 0.08)` - 默认边框（`--border-default`）
- `rgba(42, 36, 36, 0.16)` - 悬停边框（`--border-hover`）
- `#E0E0E0` - 焦点边框（`--border-focus`）
- `#D4D3D0` - 面板边框（`--border-sheet`）
- `#EBEBEB` - 分隔线（`--separator-primary`）

## 排版系统

### 字体家族

**主字体**：Gilroy
- CSS: `font-family: Gilroy, ui-sans-serif, system-ui, sans-serif;`
- 特点：几何无衬线字体，圆润现代，传达国际化气质
- 后备字体：ui-sans-serif, system-ui

### 字号层级

| 层级 | 字号 | 行高 | 字重 | 应用场景 |
|------|------|------|------|----------|
| 对话欢迎标题 | 36px | 40px | 400 | 空对话区标题（Good afternoon...） |
| 按钮文字 | 14px | - | 400/500 | 功能按钮文字 |
| 功能标签 | 14px | - | 500 | 工具标签（DeepSeek R1、Web Search） |
| 底部链接 | 13px | - | 400 | 页脚链接（About StepFun、Careers） |

**说明**：对话类页面排版层级简洁，以交互组件为主，不使用复杂的标题层级体系。

### 字重规范

- 中等（500）：按钮文字、功能标签
- 常规（400）：标题、正文、辅助文字

## 组件样式

### 按钮组件

**主 CTA 按钮（Log in）**：
```css
.btn-primary {
  background: #2A2424;
  color: #FFFFFF;
  border: none;
  border-radius: 8px;
  font-weight: 400;
  transition: all;
}

.btn-primary:hover {
  background: rgba(42, 36, 36, 0.8);
}
```

**次要按钮（New conversation）**：
```css
.btn-secondary {
  background: #FFFFFF;
  color: #2A2424;
  border: 1px solid rgba(42, 36, 36, 0.08);
  border-radius: 8px;
  font-weight: 500;
  transition: all;
}

.btn-secondary:hover {
  border-color: rgba(42, 36, 36, 0.16);
}
```

**功能标签按钮（Web Search / DeepSeek R1）**：
```css
.btn-tool {
  background: transparent;
  color: #2A2424;
  border: 1px solid rgba(42, 36, 36, 0.08);
  border-radius: 8px;
  font-weight: 400;
  font-size: 14px;
  transition: all;
}

.btn-tool:hover {
  border-color: rgba(42, 36, 36, 0.16);
  box-shadow: 0px 4px 16px 0px rgba(0, 0, 0, 0.10);
}
```

**圆形图标按钮（操作按钮）**：
```css
.btn-icon {
  background: transparent;
  color: #2A2424;
  border: none;
  border-radius: 9999px;
  padding: 6px;
  transition: all;
}

.btn-icon:hover {
  background: rgba(202, 197, 190, 0.1);
}
```

**模型选择按钮（StepClaw）**：
```css
.btn-model {
  background: transparent;
  color: #2A2424;
  border: none;
  border-radius: 10px;
  font-weight: 500;
  transition: all;
}
```

### 输入组件

**对话输入框**：
```css
.chat-input textarea {
  background: transparent;
  color: #2A2424;
  border: none;
  outline: none;
}
```

### 侧边栏组件

**侧边栏**：
```css
.sidebar {
  background: rgba(252, 252, 249, 0.98);
  border-right: 1px solid #EBEBEB;
  width: 270px;
  padding: 12px;
}
```

**顶栏**：
```css
.topbar {
  background: transparent;
  height: 64px;
  padding: 12px 20px;
}
```

### 功能标签系统

每个功能使用色彩标签区分：

| 功能 | 主色 | 填充色 | 按钮文字 |
|------|------|--------|----------|
| Web Search | #3986C5 | rgba(57,134,197,0.1) | 蓝色标签 |
| DeepSeek R1 | #3986C5 | rgba(57,134,197,0.1) | 蓝色标签+NEW角标 |
| Diligence Check | #74AD5D | rgba(116,173,93,0.1) | 绿色标签 |
| Knowledge Base | #8361B0 | rgba(131,97,176,0.1) | 紫色标签 |
| Image Creation | #E5893E | rgba(229,137,62,0.1) | 橙色标签 |
| Step Audio Studio | #E5893E | rgba(229,137,62,0.1) | 橙色标签 |
| Deploy StepClaw | #806E59 | rgba(128,110,89,0.1) | 金色标签 |

## 布局与间距

### 三栏布局

**整体结构**：
```
┌──────────┬────────────────────────┬──────────┐
│  Sidebar  │     Chat Main Area     │  Panel   │
│  270px    │     flex-1             │  (可折叠)  │
│           │                        │          │
└──────────┴────────────────────────┴──────────┘
```

### 容器设置

```css
.sidebar { width: 270px; padding: 12px; }
.topbar { height: 64px; padding: 12px 20px; }
```

### 间距系统

| 名称 | 值 | 应用场景 |
|------|-----|----------|
| 极小 | 4px | 紧凑间距 |
| 小 | 6px | 图标按钮内边距 |
| 标准 | 8px | 按钮圆角、小间距 |
| 中 | 12px | 侧边栏内边距、小按钮间距 |
| 大 | 16px | 组件间距 |
| 宽 | 20px | 顶栏水平内边距 |

### 圆角系统

| 名称 | 值 | 应用场景 |
|------|-----|----------|
| 全圆 | 9999px | 图标操作按钮 |
| 大圆角 | 10px | 模型选择按钮 |
| 标准圆角 | 8px | 功能按钮、输入框 |
| 全局默认 | 0.5rem | CSS变量 `--radius` |

## 特效与交互

### 过渡效果

```css
/* 全局默认过渡 */
transition: all;

/* 链接色过渡 */
transition: color 0.15s cubic-bezier(0.4, 0, 0.2, 1),
            background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1),
            border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1);

/* 快速过渡 */
transition: 0.15s cubic-bezier(0.4, 0, 0.2, 1);

/* 滑动过渡 */
transition: 0.3s cubic-bezier(0, 0, 0.2, 1);

/* 阴影过渡 */
transition: box-shadow 0.2s cubic-bezier(0.4, 0, 0.2, 1);

/* 高度展开 */
transition: height 0.3s ease-out;

/* 变换过渡 */
transition: transform 0.3s;
```

### 悬停效果

- 图标按钮：背景从透明 → `rgba(202,197,190,0.1)`
- 功能标签按钮：边框从 `0.08` → `0.16`，增加 `box-shadow: 0px 4px 16px 0px rgba(0,0,0,0.10)`
- CTA按钮：背景从 `#2A2424` → `rgba(42,36,36,0.8)`
- 链接：颜色从 `0.7` → `1`（`--content-primary`）

### 焦点效果

- 输入框焦点：`outline: none`
- 通用焦点环：`ring` 样式

### 滚动条样式

```css
::-webkit-scrollbar-thumb { background: rgba(0,0,0,0.2); }
::-webkit-scrollbar-thumb:hover { background: rgba(0,0,0,0.3); }
::-webkit-scrollbar-track { background: rgba(0,0,0,0.05); }
```

## 行业特色设计

### AI 对话产品行业特有元素

**行业色彩规范**：
- 暖灰棕色（#2A2424）替代传统黑色/科技蓝，传达"温暖创作"而非"冷冰冰的技术"
- 奶油白/金底色（#FCFCF9 / #F6F4F1）模拟纸张质感
- 多彩功能标签系统，用色彩区分不同AI能力

**行业组件**：
- 对话输入框：无边框、透明背景，聚焦对话内容
- 功能标签按钮：彩色标签区分AI能力类型
- 侧边栏会话列表：历史对话管理
- 模型切换器：StepClaw/DeepSeek R1等模型选择
- NEW角标：蓝色文字标签标识新功能

**行业布局特点**：
- 经典三栏对话布局（侧边栏+对话区+面板）
- 侧边栏可折叠，对话区自适应宽度
- 输入区位于底部，功能标签环绕输入框

## 使用建议

### 适用场景

- ✅ AI 对话产品界面
- ✅ 创作/写作类 SaaS 产品
- ✅ 需要温暖质感而非冷科技感的界面
- ✅ 多功能工具集成平台

### 避免场景

- ❌ 纯技术文档网站（色彩温度过高）
- ❌ 娱乐/游戏类产品（缺少活力）
- ❌ 需要强视觉冲击的落地页（过于克制）

### 最佳实践

1. 保持暖灰（#2A2424）+ 金底（#FCFCF9）的基调，不引入冷色调
2. 透明度层级是核心设计手法：0.04→0.08→0.16→0.35→0.5→0.7→0.8→1.0
3. 圆形（9999px）用于操作图标，圆角方形（8px/10px）用于内容按钮
4. 功能标签使用统一色彩体系（蓝/绿/橙/紫/红/金），每个功能一个色
5. Gilroy字体传达国际化气质，搭配系统字体回退

## CSS变量参考

```css
:root {
  /* 品牌色 */
  --content-primary: rgba(42, 36, 36, 1);       /* #2A2424 */
  --content-secondary: rgba(42, 36, 36, 0.7);
  --content-tertiary: rgba(42, 36, 36, 0.5);
  --content-disable: rgba(42, 36, 36, 0.35);
  --content-hover: rgba(42, 36, 36, 0.8);
  --content-quaterary: #BBBBBB;
  --content-reverse: #FFFFFF;

  /* 背景 */
  --background: #FCFCF9;
  --bg-gold: #F6F4F1;
  --color-fill-shallowgold: #FAF9F5;
  --color-fill-white: #FFFFFF;
  --color-fill-gray: rgba(42, 36, 36, 0.04);

  /* 边框 */
  --border-default: rgba(42, 36, 36, 0.08);
  --border-hover: rgba(42, 36, 36, 0.16);
  --border-focus: #E0E0E0;
  --border-sheet: #D4D3D0;
  --separator-primary: #EBEBEB;

  /* 悬停 */
  --hover: rgba(202, 197, 190, 0.1);
  --hover-hover: rgba(128, 110, 89, 0.08);
  --hover-new: #F3F1EE;

  /* 功能色 */
  --color-blue: #3986C5;
  --color-green: #74AD5D;
  --color-orange: #E5893E;
  --color-purple: #8361B0;
  --color-red: #D55959;
  --color-fill-gold-text: #806E59;

  /* 圆角 */
  --radius: 0.5rem;

  /* 滚动条 */
  --scrollbar-thumb: rgba(0, 0, 0, 0.2);
  --scrollbar-thumb-hover: rgba(0, 0, 0, 0.3);
  --scrollbar-track: rgba(0, 0, 0, 0.05);

  /* 渐变遮罩 */
  --message-list-mask: linear-gradient(0deg, #FCFCF9, rgba(252, 252, 249, 0));
}
```

## 设计原则总结

1. **暖灰基调**：#2A2424暖棕色 + #FCFCF9奶油白，远离冷色科技感，传达"温暖的思考伙伴"
2. **透明度即层级**：全部使用 #2A2424 的不同透明度构建视觉层级，无需多色系
3. **圆之对话**：圆形图标按钮（9999px）用于操作，圆角方形按钮（8px）用于内容，形态暗示功能类别
4. **色彩标签即分类**：蓝/绿/橙/紫/红/金六色标签系统，一个颜色对应一类AI能力
5. **克制过渡**：0.15s几乎瞬时反馈，0.3s用于结构性变化（高度/位移），不拖沓

---

**最后更新时间**：2026-04-16
**版本**：1.0.0
**行业**：科技 / AI 对话
