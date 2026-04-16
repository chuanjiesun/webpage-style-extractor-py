# BestBlogs 设计风格提取

## 项目说明

本项目是从 [BestBlogs](https://www.bestblogs.dev/) 首页提取的设计风格指南，采用网页设计风格提取器工具自动提取并人工验证。

## 提取信息

- **源网站**：https://www.bestblogs.dev/
- **提取时间**：2026-04-16
- **行业**：科技 / 内容平台
- **框架**：Tailwind CSS + Radix UI
- **主字体**：Geist + 中文回退字体栈

## 目录结构

```
bestblogs-design/
  ├── SKILL.md                # 设计风格指南（核心输出）
  ├── README.md               # 本文件
  ├── result_validation.html  # 验证页面
  └── assets/                 # 提取数据
      ├── page-info.json      # 完整页面信息数据
      ├── extraction-summary  # 提取摘要
      └── page-screenshot.png # 页面截图
```

## 关键设计要素

| 要素 | 值 |
|------|-----|
| 品牌主色 | #1A365D (Ink 墨蓝) |
| 强调色 | #D97706 (Amber 琥珀) |
| 页面底色 | #FEFDFB (Paper 奶油白) |
| 标题文字 | #1A365D / #1E293B |
| 正文文字 | #64748B |
| 主字体 | Geist |
| 圆角 | 12px (卡片) / 8px (按钮) / 6px (导航) |
| 桌面容器宽 | 1265px |
| 导航栏高度 | 57px |
