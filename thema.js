/* Farbschema-Knopf oben rechts für die Seiten neben den Hausaufgaben: System → Hell → Dunkel → System.
   Einbinden mit einer Zeile im <head> (nicht defer, damit data-theme vor dem ersten Rendern steht):
     <script src="thema.js"></script>   bzw.   <script src="../thema.js"></script>
   Die Seite definiert die Farben selbst (--accent, --sans und ihre Regeln für data-theme).
   Gleicher Speicherschlüssel wie in den Hausaufgaben, damit die Wahl mitgeht; ohne Speicher gilt sie bis zum Neuladen. */
(function () {
  var schluessel = "acs-farbschema";
  var stufen = ["system", "light", "dark"];
  var namen = { system: "System", light: "Hell", dark: "Dunkel" };
  var zeichen = { system: "◐", light: "☀︎", dark: "☾" };
  var css =
    ".thema { position: absolute; top: .6rem; right: .75rem; margin: 0; padding: .3rem .55rem; font: 600 .8rem/1 var(--sans);" +
    " color: var(--accent); background: transparent; border: 1px solid var(--accent); border-radius: 4px; cursor: pointer; }" +
    "@media print { .thema { display: none !important; } }";

  function lies() {
    try { var w = localStorage.getItem(schluessel); return stufen.indexOf(w) !== -1 ? w : "system"; }
    catch (e) { return "system"; }
  }
  function schreib(w) { try { localStorage.setItem(schluessel, w); } catch (e) { /* ohne Speicher geht es auch */ } }
  // "system" heißt: kein data-theme, dann entscheidet prefers-color-scheme im CSS der Seite
  function setze(w) {
    if (w === "system") document.documentElement.removeAttribute("data-theme");
    else document.documentElement.setAttribute("data-theme", w);
  }
  function beschrifte(k, w) { k.textContent = zeichen[w] + " " + namen[w]; k.setAttribute("aria-label", "Farbschema: " + namen[w]); }

  var wahl = lies();
  setze(wahl);

  document.addEventListener("DOMContentLoaded", function () {
    var stil = document.createElement("style");
    stil.textContent = css;
    document.head.appendChild(stil);

    var k = document.createElement("button");
    k.type = "button";
    k.className = "thema";
    beschrifte(k, wahl);
    k.addEventListener("click", function () {
      wahl = stufen[(stufen.indexOf(wahl) + 1) % stufen.length];
      setze(wahl); schreib(wahl); beschrifte(k, wahl);
    });
    // Direkt vor <main>, also nach einem Link zur Startseite: Tab-Reihenfolge links → rechts
    document.body.insertBefore(k, document.querySelector("body > main") || document.body.firstChild);
  });
})();
