# 贪吃蛇游戏快速开始指南 / Snake Game Quick Start Guide

## 中文版本 (Chinese Version)

### 🚀 快速开始

1. **启动游戏服务器**
   ```bash
   npm install
   npm run dev
   ```

2. **打开浏览器**
   - 访问 `http://localhost:3000` (或对应的端口)
   - 在顶部导航栏点击 "🐍 Snake Game" 按钮

3. **开始游戏**
   - 选择难度级别 (简单、普通、困难、地狱)
   - 点击"开始游戏"按钮或按 Enter 键

### 🎮 游戏控制

```
键盘控制方式：
┌─────────────────────┐
│  W              ↑   │  向上
│A S D  或   ← ↓ →   │  
│              ↓     │
└─────────────────────┘

P 键: 暂停/继续游戏
Enter 键: 开始游戏
```

### 📖 游戏说明

| 项目 | 说明 |
|------|------|
| 目标 | 吃掉红色食物来增长身体 |
| 计分 | 每个食物 10 分 + 身体增长奖励 5 分 |
| 失败 | 撞到墙壁或自己的身体 |
| 地图 | 环形地图（穿过边界会出现在对面） |

### 🎯 难度选择

| 难度 | 难度等级 | 推荐 |
|------|---------|------|
| 简单 | ⭐ | 初学者 |
| 普通 | ⭐⭐ | 推荐 |
| 困难 | ⭐⭐⭐ | 高手 |
| 地狱 | ⭐⭐⭐⭐ | 疯狂挑战 |

### 💾 存档系统

- ✅ 自动保存最高分到浏览器
- ✅ 跨会话保留记录
- ✅ 点击"重置"清除当前游戏数据

### 🎨 游戏特色

- 🌈 现代化 UI 设计
- ⚡ 流畅的游戏体验
- 🎵 视觉反馈效果
- 📱 响应式布局（支持手机）
- 🔄 动态难度调整

---

## English Version

### 🚀 Quick Start

1. **Start the game server**
   ```bash
   npm install
   npm run dev
   ```

2. **Open your browser**
   - Visit `http://localhost:3000` (or your configured port)
   - Click the "🐍 Snake Game" button in the top navigation

3. **Play the game**
   - Select difficulty level (Easy, Normal, Hard, Expert)
   - Click "Start Game" button or press Enter

### 🎮 Game Controls

```
Keyboard Controls:
┌─────────────────────┐
│  W              ↑   │  Move Up
│A S D  or   ← ↓ →   │  
│              ↓     │
└─────────────────────┘

P key: Pause/Resume
Enter key: Start Game
```

### 📖 Game Rules

| Item | Description |
|------|-------------|
| Objective | Eat red food to grow your snake |
| Scoring | 10 points per food + 5 bonus points for growth |
| Game Over | Hit walls or your own body |
| Map Type | Wraparound map (pass through border to reappear on opposite side) |

### 🎯 Difficulty Levels

| Level | Stars | Recommended For |
|-------|-------|-----------------|
| Easy | ⭐ | Beginners |
| Normal | ⭐⭐ | Recommended |
| Hard | ⭐⭐⭐ | Advanced Players |
| Expert | ⭐⭐⭐⭐ | Extreme Challenge |

### 💾 Save System

- ✅ Auto-saves high score to browser
- ✅ Persists across sessions
- ✅ Click "Reset" to clear current game data

### 🎨 Game Features

- 🌈 Modern UI Design
- ⚡ Smooth Gameplay Experience
- 🎵 Visual Feedback Effects
- 📱 Responsive Layout (Mobile Support)
- 🔄 Dynamic Difficulty Adjustment

---

## 📂 游戏文件结构 / File Structure

```
claude-code-runner/
├── public/
│   ├── snake.html                  # 贪吃蛇游戏主文件 / Main game file
│   ├── SNAKE_GAME_README.md       # 详细文档 / Detailed documentation
│   ├── SNAKE_GAME_QUICK_START.md  # 本文件 / This file
│   ├── index.html                  # 主应用 (已添加游戏链接)
│   └── ...
└── ...
```

---

## 🔧 技术栈 / Tech Stack

- **Frontend**: HTML5 + Canvas API + Vanilla JavaScript
- **Styling**: CSS3 with gradients and animations
- **Storage**: Browser localStorage for high scores
- **Compatibility**: Modern browsers (Chrome, Firefox, Safari, Edge)

---

## 🎮 游戏策略 / Game Strategy

### 初级 / Beginner Tips
1. 在"简单"难度上练习基本控制
2. 关注蛇头的位置，避免碰撞
3. 不要过度贪心地追逐食物

### 进阶 / Intermediate Tips
1. 预测食物的生成位置
2. 学会规划蛇的运动路径
3. 在"困难"难度上挑战自己
4. 使用墙壁作为转向点

### 高级 / Advanced Tricks
1. 掌握"蛇圈"技巧（让蛇在地图上绕圈）
2. 利用环形地图的特性
3. 优化食物追逐路径
4. 在"地狱"难度下破纪录

---

## 🐛 故障排除 / Troubleshooting

### 问题：游戏加载不了
**Solution**: 
- 确保 npm 服务器正在运行
- 检查浏览器控制台是否有错误信息
- 尝试清除浏览器缓存

### 问题：最高分没有被保存
**Solution**:
- 检查浏览器是否允许 localStorage
- 退出私密浏览模式
- 检查浏览器存储限制

### 问题：游戏运行缓慢
**Solution**:
- 关闭其他标签页
- 降低难度级别
- 检查 CPU 使用率
- 使用现代浏览器 (Chrome, Firefox)

---

## 📞 反馈和建议 / Feedback

有问题或建议？欢迎提交 Issue 或 Pull Request！

---

## 🎉 祝你游戏愉快！ / Enjoy the Game!

🐍 Happy Gaming! 🐍

---

**最后更新** / **Last Updated**: 2026年2月5日 / February 5, 2026
