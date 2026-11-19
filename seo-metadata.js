// Keep metadata aligned with the existing SPA, including Back/Forward navigation.
(function () {
  "use strict";
  var origin = "https://www.riverstickindustries.ie";
  var routes = ["/","/bark-mulch","/rubber-matting","/horse-walker-matting","/rubber-bricks"];
  function update() {
    var path = window.location.pathname.replace(/\/+$/, "") || "/";
    var known = routes.indexOf(path) !== -1;
    var canonical = document.querySelector('link[rel="canonical"]');
    var og = document.querySelector('meta[property="og:url"]');
    if (known) {
      canonical.setAttribute("href", origin + path);
      og.setAttribute("content", origin + path);
    } else {
      canonical.removeAttribute("href");
      og.removeAttribute("content");
    }
  }
  ["pushState", "replaceState"].forEach(function (method) {
    var original = window.history[method];
    window.history[method] = function () {
      var result = original.apply(this, arguments);
      update();
      return result;
    };
  });
  window.addEventListener("popstate", update);
  update();
}());

