# Doujin_Voice_Renamer
## 配置文件使用说明
## 示例配置
```json
"proxy": "http://127.0.0.1:7890",
"replace_rules": [],
"template": "[circle] title (workno)"
```

## proxy
**代理**

例如："proxy": "http://127.0.0.1:7890"

## template
**自定义模板**

"circle", "workno", "title" 和 "cv", 模板中的这四个关键字将会被程序替换

**默认模板**: "template": "workno [circle] title (cv)"

例如："template": "[circle] title (workno)"

重命名前：RJ149268 哀しみのイき人形

重命名后：[Hypnotic_Yanh] 哀しみのイき人形《催眠音声・男女版同梱》 (RJ149268)

## replace_rules
**自定义替换规则**

例如，替换标题中的标点符号：
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
1. config.json 文件使用 **UTF-8** 编码, 请不要用 Windows 系统自带的记事本进行编辑，推荐使用专业的**文本编辑器**，例如: [Notepad3](https://www.appinn.com/notepad3/), [Notepad++](https://notepad-plus-plus.org/), [vscode](https://code.visualstudio.com/)
![Notepad3](https://i.loli.net/2020/09/14/q2MvzdYAj8OxUfK.png)
2. 如需在自定义模板包含 "(cv)", 请将其放在模板字符串的末尾
  - 正确的例子: "template": "workno [circle] title (cv)"
  - 错误的例子: "template": "workno [circle] (cv) title" 这可能会导致在重命名后，文件夹名称中出现多余的空格

![示例图片](https://i.loli.net/2019/08/29/KJxOBVktrlfZ6sa.png)
