# webpage-style-extractor-py
webpage-style-extractor-py是一个页面风格提取器，根据输入的url提取页面风格信息，输出为页面风格的skill文件，便于在开发中调用提取的风格，避免大模型自由发挥导致的页面丑陋问题。

## 运行环境
本项目安装环境需要以下依赖：
 - python 
 - playwright

skill目录结构：
 ```
webpage-style-extractor-py/
  ├── SKILL.md                              # 工具使用说明
  └── scripts/                              # 提取工具（工具型SKILL特有）
      └── extract_page_info.py              # 页面信息提取脚本（含交互采样 + 详细中文注释）
```

**输出目标页面风格SKILL**：
最终输出的SKILL应包含以下目录文件：
```
<site-name>-design/
  ├── SKILL.md                   # 设计风格指南（直接包含风格元素）
  ├── README.md                  # 项目说明
  ├── result_validation.html     # 验证页面
  └── assets/                    # 提取的数据（不含脚本）
      ├── page-info.json         # 页面信息数据
      ├── extraction-summary	   # 页面提取信息摘要
      └── page-screenshot.png    # 页面截图
```


 ## 使用方法 
 1、opencode 
 将skill文件放在opencode配置目录下：
| 操作系统 | 主配置目录 |
| :--- | :--- |
| Linux / macOS | `~/.config/opencode/skills/`  |
| Windows | `%USERPROFILE%\.config\opencode\skills\`|

在opencode中执行命令`/webpage-style-extractor-py 请提取https://www.example.com/的页面信息，输出到/output/目录下`，等待执行完成就可以查看指定页面的风格SKILL。

2、trae 
在项目目录下的.trae/skills/

在对话框输入`使用技能webpage-style-extractor-py 请提取https://www.example.com/的页面信息，输出到/output/目录下`，等待执行完成就可以查看指定页面的风格SKILL。

## skill获取页面效果示例
请查看`output_skills_examples`目录下效果
