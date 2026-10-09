source "https://rubygems.org"

# 站点核心（与 _config.yml 中 theme: minima 对应）
gem "jekyll", "~> 4.3"
gem "minima", "~> 2.5"

# 插件（与 _config.yml 中 plugins: 列表对应）
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.17"
end

# 仅在 CI 的测试阶段使用：HTML / 死链检查
group :test do
  gem "html-proofer", "~> 5.0"
end

# Windows / JRuby 下时区与文件监听依赖（CI 用不到，本地开发需要）
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end
