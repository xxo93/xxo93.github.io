fetch('/feed.json')
  .then(res => res.json())
  .then(data => {
    const posts = data.items;

    document.getElementById("search-box").addEventListener("input", function(e){
      const q = e.target.value.toLowerCase();

      const result = posts.filter(p =>
        p.title.toLowerCase().includes(q)
      );

      document.getElementById("results").innerHTML =
        result.map(r => `<li><a href="${r.url}">${r.title}</a></li>`).join("");
    });
  });
