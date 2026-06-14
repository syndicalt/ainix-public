// Shared inline-SVG icon sprite (Lucide-style, stroke=currentColor).
// Injected once per page so every mockup uses identical iconography.
document.addEventListener('DOMContentLoaded', () => {
  document.body.insertAdjacentHTML('afterbegin', `
<svg class="sprite" xmlns="http://www.w3.org/2000/svg"><defs>
<symbol id="ic-runs" viewBox="0 0 24 24"><path d="M3 12h4l2 6 4-14 2 8h6"/></symbol>
<symbol id="ic-approve" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="m8.5 12 2.5 2.5 4.5-5"/></symbol>
<symbol id="ic-prov" viewBox="0 0 24 24"><path d="M12 3 5 6v5c0 4 3 7 7 9 4-2 7-5 7-9V6z"/><path d="m9 12 2 2 4-4.5"/></symbol>
<symbol id="ic-policy" viewBox="0 0 24 24"><path d="M4 6h10M18 6h2M4 12h2M10 12h10M4 18h7M15 18h5"/><circle cx="16" cy="6" r="2"/><circle cx="8" cy="12" r="2"/><circle cx="13" cy="18" r="2"/></symbol>
<symbol id="ic-artifact" viewBox="0 0 24 24"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/></symbol>
<symbol id="ic-session" viewBox="0 0 24 24"><path d="m12 3 9 5-9 5-9-5z"/><path d="m3 13 9 5 9-5"/></symbol>
<symbol id="ic-search" viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></symbol>
<symbol id="ic-shield" viewBox="0 0 24 24"><path d="M12 3 5 6v5c0 4 3 7 7 9 4-2 7-5 7-9V6z"/></symbol>
<symbol id="ic-check" viewBox="0 0 24 24"><path d="m5 12 5 5 9-11"/></symbol>
<symbol id="ic-x" viewBox="0 0 24 24"><path d="M6 6l12 12M18 6 6 18"/></symbol>
<symbol id="ic-play" viewBox="0 0 24 24"><path d="M7 5v14l11-7z"/></symbol>
<symbol id="ic-term" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="m7 9 3 3-3 3M13 15h4"/></symbol>
<symbol id="ic-file" viewBox="0 0 24 24"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/></symbol>
<symbol id="ic-arrow" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></symbol>
<symbol id="ic-chev" viewBox="0 0 24 24"><path d="m9 6 6 6-6 6"/></symbol>
<symbol id="ic-down" viewBox="0 0 24 24"><path d="m6 9 6 6 6-6"/></symbol>
<symbol id="ic-bolt" viewBox="0 0 24 24"><path d="M13 3 4 14h7l-1 7 9-11h-7z"/></symbol>
<symbol id="ic-eye" viewBox="0 0 24 24"><path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></symbol>
<symbol id="ic-flag" viewBox="0 0 24 24"><path d="M5 21V4h11l-1.5 4L16 12H5"/></symbol>
<symbol id="ic-graph" viewBox="0 0 24 24"><circle cx="6" cy="12" r="2.5"/><circle cx="18" cy="6" r="2.5"/><circle cx="18" cy="18" r="2.5"/><path d="m8 11 8-4M8 13l8 4"/></symbol>
<symbol id="ic-cmd" viewBox="0 0 24 24"><path d="M9 3a3 3 0 1 0 0 6h6a3 3 0 1 0 0-6 3 3 0 0 0-3 3v12a3 3 0 1 1-3-3h6a3 3 0 1 1 3 3"/></symbol>
<symbol id="ic-clock" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></symbol>
<symbol id="ic-user" viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M5 21c0-4 3-6 7-6s7 2 7 6"/></symbol>
<symbol id="ic-warn" viewBox="0 0 24 24"><path d="M12 4 2 20h20z"/><path d="M12 10v5M12 18v.5"/></symbol>
<symbol id="ic-lock" viewBox="0 0 24 24"><rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></symbol>
<symbol id="ic-undo" viewBox="0 0 24 24"><path d="M9 7 4 12l5 5"/><path d="M4 12h11a5 5 0 0 1 0 10h-3"/></symbol>
<symbol id="ic-filter" viewBox="0 0 24 24"><path d="M3 5h18l-7 8v6l-4-2v-4z"/></symbol>
<symbol id="ic-dot" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4" fill="currentColor" stroke="none"/></symbol>
<symbol id="ic-link" viewBox="0 0 24 24"><path d="M10 14a4 4 0 0 0 6 .5l2-2a4 4 0 0 0-6-6l-1 1"/><path d="M14 10a4 4 0 0 0-6-.5l-2 2a4 4 0 0 0 6 6l1-1"/></symbol>
</defs></svg>`);
});
