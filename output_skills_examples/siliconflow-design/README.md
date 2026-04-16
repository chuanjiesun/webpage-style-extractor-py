# 硅基流动 SiliconFlow 设计风格提取

## 项目说明

本项目是从 [SiliconFlow](https://siliconflow.cn/) 首页提取的设计风格指南，采用网页设计风格提取器工具自动提取并人工验证。

## 提取信息

- **源网站**：https://siliconflow.cn/
- **提取时间**：2026-04-16
- **行业**：科技 / AI 基础设施
- **框架**：Tailwind CSS + Ant Design (carousel)
- **主字体**：Roboto + 中文回退字体栈

## 目录结构

```
siliconflow-design/
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
| 品牌主色 | #6E29F6 |
| 标题文字 | #1E293B |
| 正文文字 | #475569 |
| 品牌渐变 | linear-gradient(to right, #252736, #6E29F6) |
| 主字体 | Roboto |
| 桌面容器宽 | 1265px |
| 导航栏高度 | 78px |
