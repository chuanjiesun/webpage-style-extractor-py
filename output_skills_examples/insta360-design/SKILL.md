---
name: insta360-design
description: Extracted design style from Insta360 official site. Dark premium tech aesthetic with cinematic imagery, pill-shaped CTAs, and bold typography. Includes complete color system, component styles, and interaction guide.
meta:
  - "industry: tech"
  - "category: consumer_electronics"
---

# Insta360 - Design Style Guide

## Overview

Insta360 (影石) is a premium consumer electronics brand specializing in 360-degree cameras and imaging devices. The website features a dark, cinematic aesthetic with bold full-bleed imagery, minimal UI chrome, and pill-shaped call-to-action buttons. The design language communicates premium quality, technological sophistication, and adventure/lifestyle branding.

**Industry**: Consumer Electronics / Technology
**Design Style**: Modern, Dark Premium, Cinematic
**Core Characteristics**:
- Dark backgrounds with high-contrast white/silver text
- Full-bleed cinematic hero imagery and product showcases
- Pill-shaped (50px radius) CTA buttons as signature UI element
- Multi-step gradient overlays for image-to-content transitions
- Subtle hover animations with product image zoom (1.05-1.1x scale)

## Color System

### Primary Color

**Brand Dark**: `#262629` (rgb(38, 38, 41))
- Usage: Primary button backgrounds, active tab indicators, hover states
- Conveys: Premium, sophisticated, authoritative
- Industry note: Near-black dark gray (not pure black) is the signature action color

**Brand Dark Variant**: `#27272A` (rgb(39, 39, 42))
- Usage: Alternative CTA backgrounds, modal confirm buttons
- Nearly identical to primary dark, used interchangeably

### Background Colors

**Pure Black**: `#000000` (rgb(0, 0, 0))
- Usage: Full-bleed hero backgrounds, dark section backgrounds
- The dominant background color (940 occurrences)

**Pure White**: `#FFFFFF` (rgb(255, 255, 255))
- Usage: Light section backgrounds, CTA button text, content areas

**Light Gray Background**: `#F8F9FC` (rgb(248, 249, 252))
- Usage: Product card backgrounds, section dividers

**Silver Gray**: `#EDEFF2` (rgb(237, 239, 242))
- Usage: Outline button borders, subtle section separators

**Medium Gray**: `#D9D9D9` (rgb(217, 217, 217))
- Usage: Borders, decorative dividers

**Deep Dark**: `#1D1D1F` (rgb(29, 29, 31))
- Usage: Footer background, deep dark sections

**Dark Gray**: `#333333` (rgb(51, 51, 51))
- Usage: Alternative dark backgrounds

### Text Colors

**Primary text hierarchy**:
- Heading/Primary: `#000000` - Main headings on light backgrounds
- Body/Dark text: `#262629` (rgb(38, 38, 41)) - Body text, labels, button text
- Secondary: `#76767F` (rgb(118, 118, 127)) - Descriptions, helper links
- Tertiary: `rgba(39, 39, 42, 0.55)` - Subtle category labels, product subtitles
- Placeholder: `#A1A1AA` (rgb(161, 161, 170)) - Very subtle text
- White: `#FFFFFF` - Text on dark backgrounds, hero overlays

### Accent Colors

**Red Accent**: `#F75A4D` (rgb(247, 90, 77))
- Usage: Notification badges, accent highlights, promotional elements

**Sky Blue**: `#0EA5E9` (rgb(14, 165, 233))
- Usage: External links, privacy policy links

**Medium Blue**: `#0066CC` (rgb(0, 102, 204))
- Usage: Phone number links

**Link Blue**: `#0000EE` (rgb(0, 0, 238))
- Usage: Default browser link color (navigation product links)

### Gradient Overlays

**Bottom Mask Gradient** (used on hero images, 11 instances):
```css
linear-gradient(0deg, 
  rgba(0,0,0,0), 
  rgba(0,0,0,0.004) 6.67%, 
  rgba(0,0,0,0.016) 13.33%, 
  rgba(0,0,0,0.03) 20%, 
  rgba(0,0,0,0.06) 26.67%, 
  rgba(0,0,0,0.094) 33.33%, 
  rgba(0,0,0,0.133) 40%, 
  rgba(0,0,0,0.176) 46.67%, 
  rgba(0,0,0,0.224) 53.33%, 
  rgba(0,0,0,0.267) 60%, 
  rgba(0,0,0,0.306) 66.67%, 
  rgba(0,0,0,0.34) 73.33%, 
  rgba(0,0,0,0.37) 80%, 
  rgba(0,0,0,0.384) 86.67%, 
  rgba(0,0,0,0.396) 93.33%, 
  rgba(0,0,0,0.4))
```
Purpose: Smooth 15-step transition from transparent to dark overlay on hero images

**Top Mask Gradient** (reverse, 19 instances):
```css
linear-gradient(360deg, 
  rgba(0,0,0,0.5), 
  rgba(0,0,0,0.494) 6.67%, 
  rgba(0,0,0,0.482) 13.33%, 
  ... fading to transparent)
```
Purpose: Top-down dark overlay for readability on cinematic images

**Gold Chat Button Gradient**:
```css
linear-gradient(277deg, rgb(255, 210, 0), rgb(255, 238, 0))
```
Purpose: Customer service chat button background

### Semi-transparent Variants

- `rgba(38, 38, 41, 0.8)` - Overlay backgrounds
- `rgba(38, 38, 41, 0.4)` - Carousel arrow backgrounds
- `rgba(38, 38, 41, 0.3)` - Secondary overlay states
- `rgba(255, 255, 255, 0.3)` - White transparent overlays
- `rgba(0, 0, 0, 0.6)` - Deep dark overlays

## Typography System

### Font Family

**Title Font**: Poppins Old
- CSS: `font-family: "Poppins Old", "Noto Sans SC", Roboto;`
- Variable: `--title-font-family`
- Usage: Section titles, product names, hero headlines, category labels

**Content Font**: Roboto
- CSS: `font-family: Roboto, "Noto Sans SC", "Poppins Old";`
- Variable: `--content-font-family`
- Usage: Body text, descriptions, UI elements

**New/Modern Font**: Poppins + MiSans VF
- CSS: `font-family: "Poppins", "MiSans VF";`
- Variable: `--new-font-family`
- Usage: Modern product sections, updated UI

**Chinese Fallback**: Noto Sans SC
- Variable: `--noto`
- Usage: Chinese character rendering across all font stacks

### Font Weight Scale (Variable Font)

| Name | Value | Variable | Usage |
|------|-------|----------|-------|
| Regular | 330 | --regular | Body text, descriptions |
| Medium | 380 | --medium | Subtle emphasis |
| Semibold | 520 | --semibold | Subheadings, labels |
| Bold | 630 | --bold | Headings, product names |
| Extrabold | 700 | --extrabold | Hero headlines, CTA emphasis |
| Black | 700 | --black | Maximum weight emphasis |

### Font Size Scale

| Level | Size | Weight | Line Height | Usage |
|-------|------|--------|-------------|-------|
| H1 | 32px | 700 | normal | Page title |
| CTA Large | 16px | 500 | - | Large buy buttons |
| CTA Small | 14px | 500-600 | - | Standard buy buttons |
| Category Label | 14px | 700 | 18px | Product category labels |
| Body | 16px | 400 | - | Body text, descriptions |
| Small | 14px | 400 | - | Secondary information |
| Tiny | 12px | 700 | - | Contact chat button |

## Component Styles

### Primary CTA Button (Pill)

```css
.btn-primary {
  background: rgb(38, 38, 41);
  color: rgb(255, 255, 255);
  border: none;
  border-radius: 50px;
  padding: 0 24px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: background 0.3s;
  display: inline-flex;
  align-items: center;
}

.btn-primary:hover {
  background: rgb(81, 81, 87);
}

.btn-primary:active {
  background: rgb(81, 81, 87);
}
```

### Primary CTA Button (Large Pill)

```css
.btn-primary-lg {
  background: rgb(38, 38, 41);
  color: rgb(255, 255, 255);
  border: none;
  border-radius: 48px;
  padding: 12px 32px;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  transition: background 0.3s;
}

.btn-primary-lg:hover {
  background: rgb(81, 81, 87);
}
```

### Outline Button (View All)

```css
.btn-outline {
  background: transparent;
  color: rgb(39, 39, 42);
  border: 1px solid rgb(228, 228, 231);
  border-radius: 50px;
  padding: 1px 6px;
  font-size: 16px;
  font-weight: 400;
  cursor: pointer;
  transition: border-color 0.2s;
}

.btn-outline:hover {
  border-color: rgb(39, 39, 42);
}
```

### Secondary Link Button

```css
.btn-link {
  color: rgb(118, 118, 127);
  text-decoration: none;
  font-size: 14px;
  transition: 0.3s;
}

.btn-link:hover {
  color: rgb(38, 38, 41);
  border-color: rgb(38, 38, 41);
}
```

### Buy Link (Text Style)

```css
.btn-buy {
  color: rgb(38, 38, 41);
  text-decoration: none;
  border-radius: 100px;
  transition: background 0.2s cubic-bezier(0.445, 0.05, 0.55, 0.95);
  cursor: pointer;
}

.btn-buy:hover {
  background: rgb(81, 81, 87);
  color: white;
}
```

### Learn More Link (Text Style)

```css
.btn-learn {
  color: rgb(255, 255, 255);
  text-decoration: none;
  border-radius: 100px;
  transition: background 0.2s;
  cursor: pointer;
}

.btn-learn:hover {
  background: rgba(255, 255, 255, 0.3);
}
```

### Contact Chat Button (Gold Gradient)

```css
.btn-contact {
  background: linear-gradient(277deg, rgb(255, 210, 0), rgb(255, 238, 0));
  color: rgb(38, 38, 41);
  border: none;
  border-radius: 51px;
  padding: 10px 24px;
  font-size: 12px;
  font-weight: 700;
  cursor: pointer;
  transition: all;
}
```

### Carousel Arrow Buttons

```css
.arrow {
  background: rgba(38, 38, 41, 0.4);
  border: none;
  cursor: pointer;
  opacity: 0;
  transition: opacity 0.5s, background 0.2s;
}

.carousel:hover .arrow {
  opacity: 1;
}

.arrow:hover {
  background: rgba(38, 38, 41, 0.3);
}

.arrow:hover img {
  transform: scale(1.3);
  transition: transform 0.2s;
}
```

### Product Card Hover

```css
.product-card .picture {
  transition: transform 0.3s;
}

.product-card:hover .picture {
  transform: scale(1.1);
}

.campaign-card .cover {
  transition: transform 0.3s;
}

.campaign-card:hover .cover {
  transform: scale(1.05);
}
```

### Support Entry Cards

```css
.support-entry {
  border-radius: 16px;
  transition: all;
  cursor: pointer;
}

.support-entry:hover .text {
  border-color: rgb(38, 38, 41);
}
```

### Tab Component

```css
.tab {
  background: rgb(38, 38, 41);
  color: white;
  cursor: pointer;
  transition: background 0.2s;
}

.tab:hover {
  background: rgb(225, 227, 230);
}

.tab.active:hover {
  background: rgb(81, 81, 87);
}
```

### Modal Confirm Button

```css
.btn-confirm {
  background: rgb(39, 39, 42);
  color: rgb(255, 255, 255);
  border: none;
  border-radius: 50px;
  padding: 0 24px;
  font-size: 16px;
  font-weight: 700;
  cursor: pointer;
  transition: all;
}
```

## Layout & Spacing

### Grid System

**Layout type**: Flexbox-based with full-width sections
The page uses a stacked section layout with each section occupying full viewport width.

### Key Layout Dimensions

| Component | Dimension |
|-----------|-----------|
| Header nav height | 64px (--header-nav-height) |
| CTA border-radius | 50px (pill shape) |
| Large CTA border-radius | 48px |
| Campaign card border-radius | 24px |
| Support entry border-radius | 16px |
| Chat button border-radius | 51px |
| Buy/Learn link border-radius | 100px (full pill) |

### Section Layout Pattern

```css
.section {
  width: 100%;
  overflow: hidden;
}

.section-content {
  max-width: 1280px;
  margin: 0 auto;
}
```

### Product Grid

Products are displayed in horizontal scroll carousels (Splide.js) rather than traditional grid layouts.

## Effects & Interactions

### Transition Specifications

```css
/* Button background transition */
transition: background 0.3s;

/* Quick interaction transition */
transition: background 0.2s;

/* Smooth bezier for buy links */
transition: background 0.2s cubic-bezier(0.445, 0.05, 0.55, 0.95);

/* Border color transition */
transition: border-color 0.2s;

/* Image zoom on hover */
transition: transform 0.3s;

/* Content fade */
transition: opacity 0.3s;

/* Full property transition */
transition: all 0.3s;

/* Slow reveal */
transition: opacity 0.5s;

/* Combined position + opacity */
transition: opacity 0.2s, bottom 0.2s;

/* Large element animation */
transition: opacity 0.6s, transform 0.6s;
```

### Hover Effects

- **Primary buttons**: Background lightens from `#262629` to `#515157`
- **Outline buttons**: Border color transitions from `#E4E4E7` to `#27272A`
- **Link buttons**: Color transitions from `#76767F` to `#262629`
- **Product images**: Scale up to 1.1x on card hover
- **Campaign images**: Scale up to 1.05x on card hover
- **Carousel arrows**: Fade in from opacity 0 to 1, icon scales to 1.3x
- **Inactive tabs**: Background changes from dark to light gray
- **Support entries**: Border color appears on text
- **Buy links** (on dark): Background fills with dark + white text

### Click Effects (Simulated)

- **CTA buttons ("Buy Now")**: Active state background `#262629` -> `#515157`
- **Brand links**: Active state color momentarily turns red `rgb(255, 0, 0)` (browser default)

### Focus Effects

- **Skip link**: No visible focus ring change
- **Splide slides**: Outline removed on focus

## Industry-Specific Design

### Consumer Electronics / Camera Brand Elements

**Cinematic presentation**:
- Full-bleed hero images with multi-step gradient overlays
- Product imagery takes center stage, UI is minimal
- Dark backgrounds make product photos pop

**Lifestyle/adventure branding**:
- Hero sections feature action/lifestyle photography
- Products shown in real-world usage contexts
- Hero text overlaid on gradient-masked images

**Product showcase patterns**:
- Horizontal scroll carousels for product categories
- Product cards with hover zoom effect on images
- Tab-based product category navigation
- Side-by-side product comparison CTA

**E-commerce CTAs**:
- "立即购买" (Buy Now) is the most prominent and repeated CTA
- "了解更多" (Learn More) as secondary action
- "产品对比" (Compare Products) as utility action
- Gold gradient chat button for customer service

**Unique Insta360 patterns**:
- 15-step gradient overlay for pixel-perfect image-to-content transitions
- Fixed customer service button with golden gradient
- Privacy/cookie consent modal with same pill-button style
- "帮我选择" (Help Me Choose) as decision-support link

## Usage Recommendations

### Suitable Scenarios

- Consumer electronics product pages
- Camera/imaging tech brand websites
- Dark-themed premium product showcases
- E-commerce sites with cinematic product imagery
- Adventure/lifestyle brand sites

### Avoid Scenarios

- Light, airy, minimalist SaaS dashboards
- Text-heavy content sites requiring high readability
- Applications needing complex form interactions
- Sites targeting young children (dark theme too serious)

### Best Practices

1. Use full-bleed imagery with gradient overlays - Insta360's 15-step gradient provides superior visual blending
2. Maintain the pill-shaped button (50px radius) as the signature CTA shape - it appears consistently across all actions
3. Keep hover states subtle - 0.3s background transitions and 1.05-1.1x image zooms are the sweet spot
4. Use `#262629` as the primary action color instead of pure black - the slight warmth adds depth
5. Reserve the gold gradient (`linear-gradient(277deg, #FFD200, #FFEE00)`) exclusively for the chat/contact button
6. Apply `cubic-bezier(0.445, 0.05, 0.55, 0.95)` for buy-button transitions - this creates a satisfying snap feel

## CSS Variables Reference

```css
:root {
  /* Font Families */
  --sans: "MiSans VF";
  --content-font-family: "Roboto", "Noto Sans SC", "Poppins Old";
  --title-font-family: "Poppins Old", "Noto Sans SC", "Roboto";
  --noto: "Noto Sans SC";
  --new-font-family: "Poppins", "MiSans VF";

  /* Font Weights (Variable Font) */
  --regular: 330;
  --medium: 380;
  --semibold: 520;
  --bold: 630;
  --extrabold: 700;
  --black: 700;

  /* Layout */
  --header-nav-height: 64px;

  /* Core Colors (not CSS variables on page, but design tokens) */
  /* Primary Dark: rgb(38, 38, 41) / #262629 */
  /* Hover Dark: rgb(81, 81, 87) / #515157 */
  /* Pure Black: #000000 */
  /* Pure White: #FFFFFF */
  /* Light BG: #F8F9FC */
  /* Silver: #EDEFF2 */
  /* Secondary Text: #76767F */
  /* Red Accent: #F75A4D */
  /* Sky Blue: #0EA5E9 */
  /* Border Outline: #E4E4E7 */
  /* Chat Gold: linear-gradient(277deg, #FFD200, #FFEE00) */
}
```

## Design Principles Summary

1. **Cinematic First**: Full-bleed imagery with professional gradient overlays takes precedence over text; UI is deliberately minimal to let visuals breathe
2. **Pill-Shape Consistency**: The 50px border-radius pill button is the unifying design element across all CTAs, creating visual rhythm and brand recognition
3. **Dark Premium**: Near-black (#262629) instead of pure black for action elements adds warmth and depth; paired with precise gradient overlays for sophistication
4. **Subtle Animation Restraint**: Only three animation types exist - background color shifts (0.2-0.3s), image scale (1.05-1.1x), and opacity fades - keeping focus on content
5. **Adventurous Lifestyle**: Photography and messaging emphasize real-world usage and adventure, with products presented as tools for capturing experiences

---

**Last Updated**: 2026-04-16
**Version**: 1.0.0
**Industry**: Consumer Electronics / Technology
