# Doujin_Voice_Renamer

### 使用说明:

**关键字**："circle", "workno", "title" 和 "cv", 模板中的这四个关键字将会被程序替换

**默认模板**: "template": "workno [circle] title (cv)"

**自定义模板**: 请修改 "config.json" 中的 "template"

例如："template": "[circle] title (workno)"

重命名前：RJ149268 哀しみのイき人形

重命名后：[Hypnotic_Yanh] 哀しみのイき人形《催眠音声・男女版同梱》 (RJ149268)

**自定义替换规则**: 请修改 "config.json" 中的 "replace_rules", 例如

```json
"replace_rules": [
    {
      "from": ":",
      "to": "："
    },
    {
      "from": "?",
      "to": "？"
    },
    {
      "from": "/",
      "to": "／"
    },
    {
      "from": "\"",
      "to": "＂"
    }
  ],
```

### 注意：
1. config.json 文件使用 UTF-8 编码, 请不要使用 Windows 系统自带的记事本进行编辑，推荐使用专业的文本编辑器进行编辑，例如: [Notepad3](https://www.appinn.com/notepad3/), [vscode](https://code.visualstudio.com/)
![Notepad3](https://i.loli.net/2020/09/14/q2MvzdYAj8OxUfK.png)
2. 如需在自定义模板包含 "(cv)", 请将其放在模板字符串的末尾
  - 正确的例子: "template": "workno [circle] title (cv)"
  - 错误的例子: "template": "workno [circle] (cv) title" 这可能会导致在重命名后，文件夹名称中出现多余的空格

![示例图片](https://i.loli.net/2019/08/29/KJxOBVktrlfZ6sa.png)
