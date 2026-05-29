# Design

## Visual Theme
复古、田园、典雅的文学小票风格。

## Color Palette
使用 OKLCH 颜色空间定义核心配色，确保色彩的纯净度与典雅感。

### 1. 专注 (Focus) - 默认主题
- **Background**: `oklch(95% 0.02 85)` (米黄色/莎草纸色)
- **Ink/Text**: `oklch(25% 0.01 85)` (深灰墨色)
- **Accent**: `oklch(40% 0.05 85)` (干枯草木色)

### 2. 静谧 (Silent)
- **Background**: `oklch(30% 0.10 260)` (深蓝/深夜色)
- **Ink/Text**: `oklch(85% 0.08 240)` (矢车菊浅蓝)
- **Accent**: `oklch(70% 0.12 250)` (月光蓝)

### 3. 沉思 (Ponder)
- **Background**: `oklch(65% 0.15 250)` (矢车菊蓝)
- **Ink/Text**: `oklch(25% 0.12 260)` (深海蓝)
- **Accent**: `oklch(90% 0.05 240)` (清晨雾蓝)

## Typography
- **Primary Serif (CN)**: `Noto Serif SC` (思源宋体) - 用于体现典雅、文学感。
- **Typewriter/Display (EN/Num)**: `Special Elite` - 用于模拟打字机印迹。
- **Body Serif (EN)**: `Times New Roman` - 经典、知性的选择。

## Components
- **The Receipt**: 具有 Papyros 纹理，底部带有 12px 间距的锯齿边缘 (`receipt-zigzag`)。
- **Option Buttons**: 圆角矩形，背景微透，选中时 `font-weight: 900` 且边框加深。
- **Theme Switcher**: 胶囊型按钮，通过反转色彩或加粗标识当前主题。

## Layout
- **Mobile First**: 9:16 比例的小票居中显示。
- **Spacing**: 遵循 4px/8px 网格系统，确保排版的节奏感。

## Motion
- **Transitions**: 主题切换使用 0.5s ease-out 过渡。
- **Confetti**: 成功推荐后触发五彩纸屑动效。
- **Reduced Motion**: 尊重系统设置，关闭不必要的闪烁动画。
