#!/usr/bin/env python3
"""Build script for Smart Money Flow blog."""
import os, json
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
ARTICLES_DIR = os.path.join(BASE, 'articles')
os.makedirs(ARTICLES_DIR, exist_ok=True)

SITE_URL = "https://smartmoneyflow.com"
SITE_NAME = "Smart Money Flow"

# Article definitions
articles = [
    {"slug":"best-side-hustles-2026","title":"10 Best Side Hustles in 2026 (I Tested All of Them)","desc":"I personally tested 10 side hustles over 6 months. Here are the real results, earnings, and honest reviews of each one for 2026.","cat":"Side Hustles","emoji":"💼","date":"2026-03-10","rt":"12 min","featured":True,"kw":"side hustles 2026, best side hustles, make money online"},
    {"slug":"freelancing-fiverr-1000-month","title":"How to Make $1000/Month with Freelancing on Fiverr","desc":"A step-by-step guide to building a profitable Fiverr freelancing business that earns $1,000+ per month.","cat":"Freelancing","emoji":"🎯","date":"2026-03-08","rt":"14 min","kw":"fiverr freelancing, make money fiverr"},
    {"slug":"google-adsense-guide","title":"Google AdSense Guide: From Zero to $500/Month","desc":"Learn how to get approved for Google AdSense and optimize your blog to earn $500+ per month.","cat":"Blogging","emoji":"📊","date":"2026-03-06","rt":"15 min","kw":"google adsense guide, adsense approval"},
    {"slug":"passive-income-ideas-beginners","title":"Best Passive Income Ideas for Beginners 2026","desc":"15 proven passive income ideas that actually work in 2026. Start earning while you sleep.","cat":"Passive Income","emoji":"💰","date":"2026-03-04","rt":"13 min","kw":"passive income ideas, passive income beginners"},
    {"slug":"youtube-monetization-guide","title":"YouTube Monetization Guide: How Much Can You Really Earn?","desc":"Real YouTube earnings data, monetization requirements, and strategies to maximize your channel revenue.","cat":"YouTube","emoji":"🎬","date":"2026-03-02","rt":"14 min","kw":"youtube monetization, youtube earnings"},
    {"slug":"affiliate-marketing-beginners-guide","title":"Affiliate Marketing for Beginners: Complete 2026 Guide","desc":"Everything about affiliate marketing — choosing programs, driving conversions, beginner-friendly guide.","cat":"Affiliate Marketing","emoji":"🔗","date":"2026-02-28","rt":"16 min","kw":"affiliate marketing beginners, affiliate guide"},
    {"slug":"start-blog-that-makes-money","title":"How to Start a Blog That Actually Makes Money","desc":"Complete roadmap to starting a profitable blog in 2026. Niche selection, setup, and monetization.","cat":"Blogging","emoji":"✍️","date":"2026-02-26","rt":"15 min","kw":"start a blog, blogging for money"},
    {"slug":"dropshipping-vs-print-on-demand","title":"Dropshipping vs Print-on-Demand: Which Is More Profitable?","desc":"Honest comparison of dropshipping and POD. Costs, profits, and which model suits you.","cat":"E-Commerce","emoji":"📦","date":"2026-02-24","rt":"11 min","kw":"dropshipping vs print on demand"},
    {"slug":"online-earning-pakistan-guide","title":"Online Earning in Pakistan: A Complete Guide for 2026","desc":"Definitive guide to making money online from Pakistan. Platforms, payments, and proven strategies.","cat":"Regional Guides","emoji":"🇵🇰","date":"2026-02-22","rt":"16 min","kw":"online earning pakistan, freelancing pakistan"},
    {"slug":"ai-tools-passive-income","title":"5 AI Tools That Help Me Earn $3,000/Month Passively","desc":"The exact AI tools I use to generate $3,000+ monthly passive income, with setup guides.","cat":"AI & Automation","emoji":"🤖","date":"2026-02-20","rt":"13 min","kw":"ai tools passive income, ai automation"},
    {"slug":"upwork-vs-fiverr-comparison","title":"Upwork vs Fiverr: Which Platform Pays More?","desc":"Detailed comparison of Upwork and Fiverr for freelancers. Fees, earnings, and recommendations.","cat":"Freelancing","emoji":"⚖️","date":"2026-02-18","rt":"11 min","kw":"upwork vs fiverr, freelancing platforms"},
    {"slug":"build-email-list-make-money","title":"How to Build an Email List and Make Money From It","desc":"Grow an email list from zero and monetize it. The most underrated income method explained.","cat":"Email Marketing","emoji":"📧","date":"2026-02-16","rt":"14 min","kw":"build email list, email marketing money"},
    {"slug":"tiktok-shop-affiliate-guide","title":"TikTok Shop Affiliate: New Way to Earn in 2026","desc":"How to earn money as a TikTok Shop affiliate. Product selection and content strategies.","cat":"Social Media","emoji":"📱","date":"2026-02-14","rt":"10 min","kw":"tiktok shop affiliate, tiktok monetization"},
    {"slug":"best-web-hosting-bloggers","title":"Best Web Hosting for Bloggers (Honest Comparison)","desc":"I tested 8 hosting providers. Honest comparison with speed tests and pricing breakdowns.","cat":"Blogging","emoji":"🌐","date":"2026-02-12","rt":"13 min","kw":"best web hosting, hosting comparison"},
    {"slug":"create-sell-digital-products","title":"How to Create and Sell Digital Products Online","desc":"From ebooks to courses to templates — create digital products that sell on autopilot.","cat":"Digital Products","emoji":"📀","date":"2026-02-10","rt":"14 min","kw":"sell digital products, digital product ideas"},
    {"slug":"cryptocurrency-beginners-guide","title":"Cryptocurrency for Beginners: Should You Invest in 2026?","desc":"Beginner-friendly crypto guide. What to buy, risks, and whether it's worth it in 2026.","cat":"Investing","emoji":"₿","date":"2026-02-08","rt":"12 min","kw":"cryptocurrency beginners, crypto investing"},
    {"slug":"remote-jobs-50-per-hour","title":"Remote Jobs That Pay $50+/Hour (No Degree Needed)","desc":"17 high-paying remote jobs without a degree. Real salaries and how to land them.","cat":"Remote Work","emoji":"🏠","date":"2026-02-06","rt":"13 min","kw":"remote jobs high paying, work from home"},
    {"slug":"how-i-made-first-10000-online","title":"How I Made My First $10,000 Online (Step by Step)","desc":"The real story of earning my first $10,000 online. Every mistake and breakthrough.","cat":"Personal Journey","emoji":"🏆","date":"2026-02-04","rt":"15 min","kw":"first 10000 online, make money story"},
    {"slug":"pinterest-marketing-free-traffic","title":"Pinterest Marketing: Drive Free Traffic to Your Blog","desc":"Use Pinterest to drive thousands of free visitors to your blog with these strategies.","cat":"Social Media","emoji":"📌","date":"2026-02-02","rt":"12 min","kw":"pinterest marketing, blog traffic"},
    {"slug":"amazon-kdp-publish-books-ai","title":"Amazon KDP: How to Publish and Sell Books with AI","desc":"Complete guide to KDP publishing with AI tools. Writing to marketing — earn royalties.","cat":"Digital Products","emoji":"📚","date":"2026-01-30","rt":"14 min","kw":"amazon kdp, self publishing, ai books"},
    {"slug":"shopify-vs-woocommerce","title":"Shopify vs WooCommerce: Best E-Commerce Platform 2026","desc":"Comprehensive comparison of Shopify and WooCommerce. Pricing, features, and recommendations.","cat":"E-Commerce","emoji":"🛒","date":"2026-01-28","rt":"12 min","kw":"shopify vs woocommerce, ecommerce platform"},
    {"slug":"instagram-monetization-guide","title":"Instagram Monetization: Beyond Just Followers","desc":"Make money on Instagram in 2026. Sponsorships, affiliates, digital products, and more.","cat":"Social Media","emoji":"📸","date":"2026-01-26","rt":"11 min","kw":"instagram monetization, instagram money"},
    {"slug":"investing-101-first-1000","title":"Investing 101: Where to Put Your First $1,000","desc":"Exactly where to invest your first $1,000. Index funds, ETFs, robo-advisors explained.","cat":"Investing","emoji":"📈","date":"2026-01-24","rt":"12 min","kw":"investing beginners, first investment"},
    {"slug":"start-youtube-channel-zero-subscribers","title":"How to Start a YouTube Channel with Zero Subscribers","desc":"Complete guide to starting YouTube from scratch. Equipment, niche, and growth tips.","cat":"YouTube","emoji":"▶️","date":"2026-01-22","rt":"14 min","kw":"start youtube channel, youtube beginners"},
    {"slug":"zero-dollar-startup-guide","title":"The $0 Startup Guide: Online Businesses You Can Start Today","desc":"12 online businesses you can start with zero money. Free tools, no investment needed.","cat":"Side Hustles","emoji":"🚀","date":"2026-01-20","rt":"13 min","kw":"start business no money, free online business"},
]

cats = {
    "Side Hustles":{"c":"#EA580C","b":"#FFF7ED"},
    "Freelancing":{"c":"#059669","b":"#D1FAE5"},
    "Blogging":{"c":"#2563EB","b":"#EFF6FF"},
    "Passive Income":{"c":"#7C3AED","b":"#F5F3FF"},
    "YouTube":{"c":"#DC2626","b":"#FEF2F2"},
    "Affiliate Marketing":{"c":"#0891B2","b":"#ECFEFF"},
    "E-Commerce":{"c":"#CA8A04","b":"#FEFCE8"},
    "Regional Guides":{"c":"#16A34A","b":"#F0FDF4"},
    "AI & Automation":{"c":"#6366F1","b":"#EEF2FF"},
    "Email Marketing":{"c":"#D946EF","b":"#FAF5FF"},
    "Social Media":{"c":"#EC4899","b":"#FDF2F8"},
    "Digital Products":{"c":"#14B8A6","b":"#F0FDFA"},
    "Investing":{"c":"#0D9488","b":"#F0FDFA"},
    "Remote Work":{"c":"#8B5CF6","b":"#F5F3FF"},
    "Personal Journey":{"c":"#F59E0B","b":"#FFFBEB"},
}

def header(active=''):
    return f'''<header class="site-header">
  <div class="header-inner">
    <a href="/" class="site-logo">
      <img src="/favicon.svg" alt="Smart Money Flow" width="36" height="36">
      <span>Smart Money Flow</span>
    </a>
    <nav>
      <ul class="nav-links" id="navLinks">
        <li><a href="/" {'class="active"' if active=='home' else ''}>Home</a></li>
        <li><a href="/about" {'class="active"' if active=='about' else ''}>About</a></li>
        <li><a href="/contact" {'class="active"' if active=='contact' else ''}>Contact</a></li>
        <li><button class="search-toggle" onclick="toggleSearch()" aria-label="Search"><svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><circle cx="8" cy="8" r="6"/><line x1="13" y1="13" x2="17" y2="17"/></svg></button></li>
      </ul>
    </nav>
    <button class="mobile-menu-btn" onclick="toggleMobileMenu()" aria-label="Menu">
      <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
    </button>
  </div>
</header>'''

def footer():
    return '''<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="/" class="site-logo" style="color:#fff;margin-bottom:8px;display:inline-flex"><img src="/favicon.svg" alt="" width="32" height="32"><span style="-webkit-text-fill-color:#fff">Smart Money Flow</span></a>
        <p>Real strategies to earn online &mdash; tested, honest, actionable. Helping you build sustainable income streams since 2024.</p>
      </div>
      <div class="footer-col"><h4>Quick Links</h4><ul><li><a href="/">Home</a></li><li><a href="/about">About</a></li><li><a href="/contact">Contact</a></li><li><a href="/disclosure">Disclosure</a></li></ul></div>
      <div class="footer-col"><h4>Categories</h4><ul><li><a href="/#articles">Side Hustles</a></li><li><a href="/#articles">Freelancing</a></li><li><a href="/#articles">Passive Income</a></li><li><a href="/#articles">Blogging</a></li></ul></div>
      <div class="footer-col"><h4>Legal</h4><ul><li><a href="/privacy">Privacy Policy</a></li><li><a href="/disclaimer">Disclaimer</a></li><li><a href="/disclosure">Affiliate Disclosure</a></li><li><a href="/contact">Contact Us</a></li></ul></div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2024-2026 Smart Money Flow. All rights reserved.</p>
      <div class="footer-social"><a href="#" aria-label="Twitter">𝕏</a> <a href="#" aria-label="YouTube">▶</a> <a href="#" aria-label="Pinterest">📌</a></div>
    </div>
  </div>
</footer>'''

def search_overlay():
    return '''<div class="search-overlay" id="searchOverlay"><div class="search-box"><input type="text" id="searchInput" placeholder="Search articles..." autocomplete="off" oninput="performSearch(this.value)"><div class="search-results" id="searchResults"></div></div></div>'''

def search_script():
    items = json.dumps([{"s":a["slug"],"t":a["title"],"d":a["desc"],"c":a["cat"]} for a in articles])
    return f'''<script>
var SA={items};
function toggleSearch(){{var o=document.getElementById('searchOverlay');o.classList.toggle('active');if(o.classList.contains('active'))document.getElementById('searchInput').focus()}}
function toggleMobileMenu(){{document.getElementById('navLinks').classList.toggle('open')}}
document.addEventListener('keydown',function(e){{if(e.key==='Escape'){{document.getElementById('searchOverlay').classList.remove('active');document.getElementById('navLinks').classList.remove('open')}}if((e.ctrlKey||e.metaKey)&&e.key==='k'){{e.preventDefault();toggleSearch()}}}});
document.getElementById('searchOverlay')?.addEventListener('click',function(e){{if(e.target===this)this.classList.remove('active')}});
function performSearch(q){{var r=document.getElementById('searchResults');if(!q||q.length<2){{r.innerHTML='';return}}var l=q.toLowerCase();var m=SA.filter(function(a){{return a.t.toLowerCase().includes(l)||a.d.toLowerCase().includes(l)||a.c.toLowerCase().includes(l)}});r.innerHTML=m.length?m.map(function(a){{return'<div class="search-result-item"><a href="/articles/'+a.s+'">'+a.t+'</a><p>'+a.d.slice(0,100)+'...</p></div>'}}).join(''):'<p style="padding:16px;color:#9CA3AF">No articles found.</p>'}}
window.addEventListener('scroll',function(){{var b=document.querySelector('.back-to-top');if(b)b.classList.toggle('visible',window.scrollY>400)}});
</script>'''

def head(title, desc, url, typ='website'):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="Alex Rahman">
<link rel="canonical" href="{SITE_URL}{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE_URL}{url}">
<meta property="og:type" content="{typ}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="manifest" href="/manifest.json">
<meta name="theme-color" content="#2563EB">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="/style.css">
</head>'''

print("Building Smart Money Flow...")

# ============ HOMEPAGE ============
unique_cats = list(dict.fromkeys(a["cat"] for a in articles))
feat = next((a for a in articles if a.get("featured")), None)
regs = [a for a in articles if not a.get("featured")]

def card(a, featured=False):
    c = cats.get(a["cat"],{"c":"#2563EB","b":"#EFF6FF"})
    from datetime import datetime as dt
    d = dt.strptime(a["date"],"%Y-%m-%d").strftime("%b %d, %Y")
    return f'''<article class="article-card{' featured' if featured else ''}" data-category="{a['cat']}">
  <div class="card-image">{a['emoji']}</div>
  <div class="card-body">
    <span class="card-category" style="color:{c['c']};background:{c['b']}">{a['cat']}</span>
    <h3 class="card-title"><a href="/articles/{a['slug']}">{a['title']}</a></h3>
    <p class="card-excerpt">{a['desc']}</p>
    <div class="card-meta"><span>Alex Rahman &middot; {d}</span><span class="read-time">📖 {a['rt']} read</span></div>
  </div>
</article>'''

cat_pills = '<button class="category-pill active" onclick="filterArticles(\'all\')">All Topics</button>\n' + '\n'.join(f'<button class="category-pill" onclick="filterArticles(\'{c}\')">{c}</button>' for c in unique_cats)
all_cards = ""
if feat: all_cards += card(feat, True) + "\n"
all_cards += "\n".join(card(a) for a in regs)

homepage = f'''{head(SITE_NAME+" — Real Strategies to Earn Online","Tested, honest, actionable strategies to earn money online. Side hustles, passive income, freelancing, blogging, and more.","/")}
<body>
{header('home')}
{search_overlay()}
<section class="hero"><div class="container">
<h1>Build Real Income <span class="accent">Online</span></h1>
<p>Tested strategies, honest reviews, and actionable guides to help you earn money online &mdash; written by someone who actually does it.</p>
<a href="#articles" class="hero-cta">Explore Guides &darr;</a>
</div></section>
<div class="container"><div class="ad-zone ad-zone-header">Advertisement</div></div>
<section class="category-section"><div class="container"><div class="category-grid">
{cat_pills}
</div></div></section>
<section class="articles-section" id="articles"><div class="container">
<h2>Latest Articles</h2>
<div class="articles-grid">
{all_cards}
</div></div></section>
<section class="newsletter-section"><div class="container">
<h2>💌 Join 5,000+ Smart Earners</h2>
<p>Get weekly tips on making money online &mdash; no spam, no fluff, just actionable strategies.</p>
<form class="newsletter-form" onsubmit="event.preventDefault();alert('Thanks for subscribing!')"><input type="email" placeholder="Enter your email" required><button type="submit">Subscribe Free</button></form>
</div></section>
{footer()}
<button class="back-to-top" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">↑</button>
{search_script()}
<script>
function filterArticles(c){{document.querySelectorAll('.category-pill').forEach(function(p){{p.classList.remove('active')}});event.target.classList.add('active');document.querySelectorAll('.article-card').forEach(function(card){{card.style.display=(c==='all'||card.dataset.category===c)?'':'none'}})}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"WebSite","name":"{SITE_NAME}","url":"{SITE_URL}","description":"Real strategies to earn online — tested, honest, actionable","publisher":{{"@type":"Person","name":"Alex Rahman"}}}}
</script>
</body></html>'''

with open(os.path.join(BASE, 'index.html'), 'w') as f:
    f.write(homepage)
print("✅ index.html")

# ============ SITEMAP ============
sitemap_entries = f'''<url><loc>{SITE_URL}/</loc><changefreq>daily</changefreq><priority>1.0</priority></url>
<url><loc>{SITE_URL}/about</loc><changefreq>monthly</changefreq><priority>0.7</priority></url>
<url><loc>{SITE_URL}/contact</loc><changefreq>monthly</changefreq><priority>0.5</priority></url>
<url><loc>{SITE_URL}/privacy</loc><changefreq>yearly</changefreq><priority>0.3</priority></url>
<url><loc>{SITE_URL}/disclaimer</loc><changefreq>yearly</changefreq><priority>0.3</priority></url>
<url><loc>{SITE_URL}/disclosure</loc><changefreq>yearly</changefreq><priority>0.3</priority></url>
''' + '\n'.join(f'<url><loc>{SITE_URL}/articles/{a["slug"]}</loc><lastmod>{a["date"]}</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>' for a in articles)

sitemap = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{sitemap_entries}
</urlset>'''
with open(os.path.join(BASE, 'sitemap.xml'), 'w') as f:
    f.write(sitemap)
print("✅ sitemap.xml")

print("\\n✅ Build script foundation complete!")
print("Static pages and articles will be written separately.")
