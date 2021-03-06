# issues-api

一个通过解析 issues 中第一段 `JSON` 代码块并生成 API 加速访问的工具。解决了直接调用 GitHub API 频率有限制以及速度过慢的问题。

测试地址： https://issues-api.vercel.app/xaoxuu

## 使用方法

1. [复制](https://github.com/xaoxuu/issues-api/generate) 或者 fork 本仓库
2. 修改 `_config.yml` 中的配置。

### 测试是否配置成功

1. 新建 issue 并按照模板要求填写提交。
2. 等待 Action 运行完毕，检查 `output.json` 文件内容是否正确，如果正确则表示已经配置成功。

### 前端使用方法

```
{% friends repo:xaoxuu/friends %}
{% sites repo:xaoxuu/hexo-theme-stellar-examples %}
```

目前已经适配的博客有：

- [Stellar](https://github.com/xaoxuu/hexo-theme-stellar)

如果您的博客主题（不仅限于 Hexo 主题）也适配了，欢迎提 PR 修改此 README 文件。博客主题适配思路：通过调用 API 得到数据，解析并生成 HTML 代码，参考：

- [通过 friends.js 解析并生成 HTML 代码](https://github.com/xaoxuu/hexo-theme-stellar/blob/main/source/js/plugins/friends.js)
- [编写 friends 标签插件，方便用户使用](https://github.com/xaoxuu/hexo-theme-stellar/blob/main/scripts/tags/friends.js)

## 如果需要自己部署 Vercel API

[![Deploy to Vercel](https://camo.githubusercontent.com/f209ca5cc3af7dd930b6bfc55b3d7b6a5fde1aff/68747470733a2f2f76657263656c2e636f6d2f627574746f6e)](https://vercel.com/import/project?template=https://github.com/xaoxuu/issues-api)

然后访问 `https://issues-api.vercel.app/yourname`

如果仓库为其他名称，例如 `examples`，那么需要指定仓库名：
```
https://issues-api.vercel.app/yourname/examples
```

如果仓库默认分支不是 `main`，那么需要指定分支：
```
https://issues-api.vercel.app/yourname/examples/master
```

前端使用方法示例：

```
{% friends repo:yourname/examples api:https://issues-api.vercel.app/yourname/examples %}
```

## 感谢

非常感谢 [@Zfour](https://github.com/Zfour) 的 python 代码和耐心指导！
文章链接：[《教程：github/gitee issues的友链信息自动生成json及api调用》](https://zfe.space/post/python-issues-api.html)
