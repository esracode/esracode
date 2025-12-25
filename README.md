# Linktree-style GitHub Pages

A simple, clean Linktree-style landing page for GitHub Pages.

## Features

- 🎨 Modern, gradient background design
- 📱 Fully responsive
- ⚡ Fast and lightweight
- 🎯 Easy to customize

## Setup for GitHub Pages

1. Push this repository to GitHub
2. Go to your repository settings
3. Navigate to "Pages" in the sidebar
4. Select your branch (usually `main` or `master`)
5. Your site will be available at `https://yourusername.github.io/repository-name`

## Customization

### Update Profile Information

Edit `index.html` and update:
- Profile picture URL (replace the placeholder image)
- Your name
- Your bio
- Add/remove/edit link buttons

### Update Links

Replace the `href="#"` in each link button with your actual URLs:

```html
<a href="https://yourwebsite.com" class="link-button" target="_blank" rel="noopener noreferrer">
    <span class="link-text">Website</span>
</a>
```

### Customize Colors

Edit `style.css` to change the gradient colors. Look for:

```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

Replace the hex colors (`#667eea` and `#764ba2`) with your preferred colors.

## License

Free to use and modify as you wish!

