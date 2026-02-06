# 🐍 贪吃蛇游戏 - 快速访问指南

## 欢迎！Welcome! 🎮

这个项目已经集成了一个现代化的贪吃蛇小游戏。请按照以下步骤快速开始游戏！

---

## ⚡ 最快 3 步开始游戏

### 1️⃣ 安装依赖
```bash
npm install
```

### 2️⃣ 启动服务器
```bash
npm run dev
```

### 3️⃣ 打开游戏
- 在浏览器访问 `http://localhost:3000`
- 点击顶部导航的 **"🐍 Snake Game"** 按钮
- 或直接访问 `http://localhost:3000/snake.html`

---

## 📚 文档导航

| 文档 | 位置 | 用途 |
|------|------|------|
| 🚀 **安装指南** | [SNAKE_GAME_INSTALLATION.md](./SNAKE_GAME_INSTALLATION.md) | 完整的安装和功能介绍 |
| 📖 **详细文档** | [public/SNAKE_GAME_README.md](./public/SNAKE_GAME_README.md) | 游戏规则、技巧、自定义方法 |
| ⚡ **快速开始** | [public/SNAKE_GAME_QUICK_START.md](./public/SNAKE_GAME_QUICK_START.md) | 双语快速开始指南 |
| 🎮 **游戏文件** | [public/snake.html](./public/snake.html) | 完整的游戏代码 |

---

## 🎮 游戏控制

```
键盘控制：
┌─────────────────────┐
│  W              ↑   │
│A S D  或   ← ↓ →   │
│              ↓     │
└─────────────────────┘

其他按键：
P  = 暂停/继续
Enter = 开始游戏
```

---

## 🎯 游戏难度

选择你喜欢的难度：
- **简单** (⭐) - 初学者友好
- **普通** (⭐⭐) - 推荐模式（默认）
- **困难** (⭐⭐⭐) - 高手级别
- **地狱** (⭐⭐⭐⭐) - 极限挑战

---

## ✨ 游戏特点

✅ **现代化界面** - 精美的渐变背景和卡片设计  
✅ **流畅体验** - 使用 Canvas 高性能渲染  
✅ **多难度** - 4 个难度等级可选  
✅ **自动加速** - 分数增加时游戏难度自动提升  
✅ **分数记录** - 自动保存历史最高分  
✅ **响应式** - 支持各种屏幕尺寸  
✅ **无依赖** - 纯 HTML + CSS + JavaScript  

---

## 🚀 项目结构

```
claude-code-runner/
│
├── 📄 SNAKE_GAME_INSTALLATION.md  ← 详细安装指南
├── 📄 README.md                    ← 项目原 README
│
└── public/
    ├── 🎮 snake.html              ← 游戏主文件 ⭐
    ├── 📖 SNAKE_GAME_README.md     ← 游戏详细文档
    ├── 📖 SNAKE_GAME_QUICK_START.md ← 快速开始指南
    └── 📄 index.html               ← 已添加游戏链接
```

---

## 🎁 功能列表

### 基础游戏
- ✅ 蛇的移动和控制
- ✅ 食物生成和碰撞
- ✅ 身体增长和分数
- ✅ 游戏结束检测

### 高级功能
- ✅ 4 个难度等级
- ✅ 暂停/继续功能
- ✅ 历史最高分记录
- ✅ 游戏统计信息
- ✅ 动态难度调整
- ✅ 环形地图包裹

### 用户界面
- ✅ 实时分数显示
- ✅ 身体长度计数
- ✅ 最高分排行
- ✅ 暂停界面覆盖
- ✅ 游戏结束弹窗
- ✅ 操作提示说明

---

## 💡 快速技巧

### 初学者提示
1. 从"简单"难度开始熟悉控制
2. 不要让蛇的身体太长时做复杂转向
3. 预留足够的空间来转向

### 进阶技巧
1. 学会使用"蛇圈"策略（蛇绕圈移动）
2. 利用环形地图从一边进另一边出
3. 提前预判食物会出现的位置

### 高分秘诀
1. 在困难和地狱难度上多练习
2. 掌握精准的转向时机
3. 保持稳定的节奏，不要过急

---

## 🔧 自定义游戏

### 修改游戏速度
编辑 `public/snake.html` 中的 `DIFFICULTIES` 对象：
```javascript
const DIFFICULTIES = {
    easy: { speed: 6, color: '#90EE90' },
    normal: { speed: 8, color: '#00FF00' },
    hard: { speed: 12, color: '#FFD700' },
    expert: { speed: 16, color: '#FF6347' }
};
```

### 改变网格大小
```javascript
const GRID_SIZE = 20;  // 改为 15、25 等
```

### 调整分数规则
```javascript
gameState.score += 10;  // 改为其他值
```

更多自定义方法请查看 [SNAKE_GAME_README.md](./public/SNAKE_GAME_README.md)

---

## 🌍 浏览器支持

| 浏览器 | 支持 | 推荐 |
|--------|------|------|
| Chrome | ✅ | ⭐⭐⭐⭐⭐ 推荐 |
| Firefox | ✅ | ⭐⭐⭐⭐ |
| Safari | ✅ | ⭐⭐⭐⭐ |
| Edge | ✅ | ⭐⭐⭐⭐ |
| 移动浏览器 | ✅ | ⭐⭐⭐ |

---

## 🐛 常见问题

### Q: 游戏打不开
**A:** 确保 npm 服务器已启动，尝试：
```bash
npm run dev
```
然后访问 `http://localhost:3000`

### Q: 最高分没有保存
**A:** 检查浏览器是否禁用了 localStorage，或者你在私密浏览模式

### Q: 游戏运行缓慢
**A:** 
- 关闭其他标签页
- 使用现代浏览器 (Chrome 优先)
- 选择较低的难度级别
- 检查 CPU 占用情况

### Q: 如何重置分数
**A:** 点击游戏中的"重置"按钮，或在浏览器开发者工具执行：
```javascript
localStorage.clear()
```

---

## 📊 游戏统计

创建日期：2026 年 2 月 5 日  
文件数：4 个 (1 游戏 + 3 文档)  
代码行：800+ 行  
文件大小：约 50 KB (非压缩)  
依赖数：0 (零依赖！)  

---

## 🎯 下一步

### 立即开始
```bash
npm install && npm run dev
```

### 查看详细文档
- 🎮 [游戏详细文档](./public/SNAKE_GAME_README.md)
- 📖 [快速开始指南](./public/SNAKE_GAME_QUICK_START.md)
- 📄 [完整安装指南](./SNAKE_GAME_INSTALLATION.md)

### 分享你的成绩
- 在"地狱"难度获得 1000+ 分？
- 创建排行榜并分享你的高分！

---

## 🎉 准备好了吗？

```
┌─────────────────────────────────────┐
│                                     │
│         🐍 准备好了吗？🐍           │
│                                     │
│  打开游戏，开始你的贪吃蛇冒险！   │
│                                     │
│   npm run dev → 然后按链接打开     │
│                                     │
└─────────────────────────────────────┘
```

---

## 🙌 致谢

感谢选择 Claude Code Runner 项目！  
希望你喜欢这个贪吃蛇游戏！

**Happy Gaming! 🎮✨**

---

有任何问题或建议？  
📧 查看项目文档或提交 Issue

**祝你游戏愉快！** 🐍🎯
