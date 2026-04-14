<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dashboard Opname Inventori Kartu ATM — Cabang Roxi</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Segoe UI',Arial,sans-serif;font-size:14px;background:#F4F6F9;color:#1a1a2e;min-height:100vh}
.app{display:flex;min-height:100vh}

/* LOGIN */
#loginScreen{position:fixed;inset:0;background:#F4F6F9;display:flex;align-items:center;justify-content:center;z-index:9999}
#loginScreen.hidden{display:none}
.login-card{background:#fff;border:1px solid #e8eaf0;border-radius:16px;padding:40px 36px;width:100%;max-width:400px}
.login-logo{display:flex;align-items:center;gap:12px;margin-bottom:28px}
.login-logo-mark{width:42px;height:42px;border-radius:12px;background:#003087;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.login-logo-mark span{color:#fff;font-size:15px;font-weight:700}
.login-logo-text h2{font-size:15px;font-weight:700;color:#1a1a2e;margin:0}
.login-logo-text p{font-size:12px;color:#888;margin:2px 0 0}
.login-title{font-size:20px;font-weight:700;color:#1a1a2e;margin-bottom:6px}
.login-sub{font-size:13px;color:#888;margin-bottom:28px}
.login-label{font-size:12px;font-weight:600;color:#555;margin-bottom:6px;display:block}
.login-input{width:100%;padding:10px 14px;font-size:14px;border:1px solid #dde2f0;border-radius:8px;font-family:inherit;outline:none;transition:border .15s;margin-bottom:16px;background:#fff;color:#1a1a2e}
.login-input:focus{border-color:#003087;box-shadow:0 0 0 3px rgba(0,48,135,.08)}
.login-input.err{border-color:#e53935;box-shadow:0 0 0 3px rgba(229,57,53,.08)}
.login-pw-wrap{position:relative;margin-bottom:24px}
.login-pw-wrap .login-input{margin-bottom:0;padding-right:44px}
.toggle-pw{position:absolute;right:12px;top:50%;transform:translateY(-50%);background:none;border:none;cursor:pointer;color:#aaa;font-size:16px;padding:4px;line-height:1}
.toggle-pw:hover{color:#555}
.login-btn{width:100%;padding:12px;font-size:14px;font-weight:700;background:#003087;color:#fff;border:none;border-radius:8px;cursor:pointer;font-family:inherit;transition:background .15s;letter-spacing:.02em}
.login-btn:hover{background:#00205f}
.login-btn:active{transform:scale(.98)}
.login-btn:disabled{background:#9ab0d8;cursor:not-allowed}
.login-error{display:none;background:#fff5f5;border:1px solid #ffcdd2;color:#c62828;font-size:12px;padding:10px 14px;border-radius:8px;margin-bottom:16px}
.login-error.show{display:block}
.login-footer{margin-top:20px;text-align:center;font-size:11px;color:#bbb}
.login-hint{margin-top:16px;background:#f0f4ff;border:1px solid #c8d8ff;border-radius:8px;padding:10px 14px;font-size:12px;color:#555}
.login-hint strong{color:#003087}

/* LOGOUT BUTTON in topbar */
.btn-logout{padding:6px 14px;font-size:12px;border:1px solid #dde2f0;border-radius:8px;cursor:pointer;background:#fff;color:#555;font-family:inherit;font-weight:600;transition:all .12s}
.btn-logout:hover{background:#fff5f5;border-color:#ffcdd2;color:#c62828}

/* SIDEBAR */
.sidebar{width:230px;flex-shrink:0;background:#fff;border-right:1px solid #e8eaf0;display:flex;flex-direction:column;position:sticky;top:0;height:100vh;overflow-y:auto}
.sidebar-logo{padding:22px 20px 18px;border-bottom:1px solid #e8eaf0}
.logo-mark{width:36px;height:36px;border-radius:10px;background:#003087;display:flex;align-items:center;justify-content:center;margin-bottom:10px}
.logo-mark span{color:#fff;font-size:13px;font-weight:700;letter-spacing:.5px}
.logo-name{font-size:14px;font-weight:600;color:#1a1a2e;line-height:1.3}
.logo-sub{font-size:11px;color:#888;margin-top:2px}
.nav{padding:14px 0;flex:1}
.nav-section{padding:5px 18px 3px;font-size:10px;font-weight:600;color:#aaa;text-transform:uppercase;letter-spacing:.1em;margin-top:8px}
.nav-item{display:flex;align-items:center;gap:10px;padding:9px 18px;cursor:pointer;font-size:13px;color:#555;border-left:3px solid transparent;transition:all .15s;text-decoration:none}
.nav-item:hover{background:#f0f4ff;color:#003087}
.nav-item.active{color:#003087;background:#eef3ff;border-left:3px solid #003087;font-weight:600}
.nav-icon{width:16px;height:16px;flex-shrink:0}
.sidebar-footer{padding:14px 18px;border-top:1px solid #e8eaf0}
.user-row{display:flex;align-items:center;gap:10px}
.avatar{width:32px;height:32px;border-radius:50%;background:#eef3ff;color:#003087;font-size:12px;font-weight:600;display:flex;align-items:center;justify-content:center;flex-shrink:0;border:1.5px solid #c8d8ff}
.user-name{font-size:12px;font-weight:600;color:#1a1a2e}
.user-role{font-size:11px;color:#888}

/* MAIN */
.main{flex:1;display:flex;flex-direction:column;min-width:0}
.topbar{height:56px;background:#fff;border-bottom:1px solid #e8eaf0;display:flex;align-items:center;justify-content:space-between;padding:0 28px;flex-shrink:0;position:sticky;top:0;z-index:10}
.topbar-title{font-size:16px;font-weight:600;color:#1a1a2e}
.topbar-meta{font-size:12px;color:#888;margin-top:2px}
.topbar-right{display:flex;align-items:center;gap:10px}
.badge{font-size:11px;padding:4px 12px;border-radius:20px;font-weight:600}
.badge-approved{background:#e8f5e9;color:#2e7d32}
.badge-date{background:#eef3ff;color:#003087}
.content{flex:1;padding:24px 28px}
.page{display:none}
.page.active{display:block}

/* KPI */
.kpi-row{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:22px}
.kpi{background:#fff;border-radius:10px;padding:16px 18px;border:1px solid #e8eaf0}
.kpi-label{font-size:11px;color:#888;text-transform:uppercase;letter-spacing:.05em;margin-bottom:8px;font-weight:500}
.kpi-val{font-size:26px;font-weight:700;line-height:1}
.kpi-sub{font-size:11px;color:#aaa;margin-top:5px}
.kpi-val.blue{color:#003087}
.kpi-val.green{color:#2e7d32}
.kpi-val.red{color:#c62828}
.kpi-val.amber{color:#e65100}

/* GRID */
.grid2{display:grid;grid-template-columns:1.5fr 1fr;gap:18px;margin-bottom:18px}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-bottom:18px}
.grid2b{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-bottom:18px}

/* CARD */
.card{background:#fff;border:1px solid #e8eaf0;border-radius:12px;padding:18px 20px}
.card-hdr{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px}
.card-title{font-size:11px;font-weight:600;color:#888;text-transform:uppercase;letter-spacing:.07em}
.chart-box{position:relative;width:100%}

/* LEGEND */
.leg{display:flex;flex-wrap:wrap;gap:14px;margin-bottom:12px}
.leg-i{display:flex;align-items:center;gap:5px;font-size:12px;color:#666}
.leg-sq{width:11px;height:11px;border-radius:3px;flex-shrink:0}

/* ALERT */
.alert{display:flex;align-items:flex-start;gap:12px;padding:12px 14px;border-radius:10px;margin-bottom:10px}
.alert-red{background:#fff5f5;border:1px solid #ffcdd2}
.alert-amber{background:#fff8e1;border:1px solid #ffe082}
.alert-icon{width:22px;height:22px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:1px;font-size:13px;font-weight:700}
.alert-icon-red{background:#c62828;color:#fff}
.alert-icon-amber{background:#ef6c00;color:#fff}
.alert-title{font-size:13px;font-weight:600;margin-bottom:3px}
.alert-title-red{color:#b71c1c}
.alert-title-amber{color:#bf360c}
.alert-body{font-size:12px}
.alert-body-red{color:#c62828}
.alert-body-amber{color:#e65100}

/* TABLE */
.tbl-wrap{border:1px solid #e8eaf0;border-radius:10px;overflow:hidden}
.tbl-scroll{max-height:320px;overflow-y:auto}
table{width:100%;border-collapse:collapse;font-size:13px}
th{font-size:11px;font-weight:600;color:#888;text-align:left;padding:10px 12px;border-bottom:1px solid #e8eaf0;background:#fafafa;position:sticky;top:0;white-space:nowrap}
td{padding:9px 12px;border-bottom:1px solid #f0f2f5;color:#1a1a2e;white-space:nowrap}
tr:last-child td{border-bottom:none}
tr:hover td{background:#f8f9ff}
tr.total-row td{font-weight:600;background:#f0f4ff}

/* PILLS */
.pill-ok{display:inline-flex;align-items:center;gap:4px;font-size:11px;color:#2e7d32;background:#e8f5e9;padding:3px 10px;border-radius:20px;font-weight:500}
.pill-err{display:inline-flex;align-items:center;gap:4px;font-size:11px;color:#c62828;background:#fff5f5;padding:3px 10px;border-radius:20px;font-weight:500}
.dot{width:6px;height:6px;border-radius:50%;display:inline-block}
.dot-g{background:#43a047}
.dot-r{background:#e53935}
.pill-chip{display:inline-block;font-size:11px;padding:2px 9px;border-radius:10px;background:#f0f4ff;color:#003087;font-weight:500}
.pill-cl{display:inline-block;font-size:11px;padding:2px 9px;border-radius:10px;background:#fff3e0;color:#e65100;font-weight:500}
.pill-mag{display:inline-block;font-size:11px;padding:2px 9px;border-radius:10px;background:#f3e5f5;color:#6a1b9a;font-weight:500}

/* FILTER */
.filter-row{display:flex;gap:8px;margin-bottom:14px;flex-wrap:wrap}
.fbtn{padding:5px 14px;font-size:12px;border:1px solid #dde2f0;border-radius:20px;cursor:pointer;background:#fff;color:#555;font-family:inherit;transition:all .12s}
.fbtn:hover{background:#f0f4ff;border-color:#b0c0e8}
.fbtn.on{background:#003087;color:#fff;border-color:#003087;font-weight:600}

/* PROGRESS */
.pb-row{margin-bottom:10px}
.pb-hdr{display:flex;justify-content:space-between;font-size:12px;color:#444;margin-bottom:5px}
.pb-track{background:#f0f2f5;border-radius:6px;height:8px;overflow:hidden}
.pb-fill{height:8px;border-radius:6px}

/* SECTION SEP */
.sec-sep{font-size:11px;font-weight:600;color:#888;text-transform:uppercase;letter-spacing:.07em;padding:0 0 8px;border-bottom:1px solid #e8eaf0;margin:20px 0 14px}

/* FOOTER */
.page-footer{margin-top:28px;padding:16px 0 4px;border-top:1px solid #e8eaf0;display:flex;justify-content:space-between;align-items:center}
.footer-left{font-size:12px;color:#aaa}
.footer-right{display:flex;gap:8px}
.btn-export{padding:7px 16px;font-size:12px;border:1px solid #dde2f0;border-radius:8px;cursor:pointer;background:#fff;color:#003087;font-family:inherit;font-weight:600;transition:all .12s}
.btn-export:hover{background:#003087;color:#fff;border-color:#003087}

/* PRINT */
@media print{
  .sidebar,.topbar,.filter-row,.btn-export,.page-footer{display:none!important}
  .main{padding:0}
  .content{padding:10px}
  .page{display:block!important}
  .card{break-inside:avoid}
}
</style>
</head>
<body>
<!-- LOGIN SCREEN -->
<div id="loginScreen">
  <div class="login-card">
    <div class="login-logo">
      <div class="login-logo-mark"><span>BRI</span></div>
      <div class="login-logo-text">
        <h2>Opname Inventori Kartu ATM</h2>
        <p>Sistem Manajemen Opname &mdash; Cabang Roxi</p>
      </div>
    </div>
    <div class="login-title">Masuk ke Dashboard</div>
    <div class="login-sub">Silakan masukkan kredensial Anda untuk melanjutkan.</div>

    <div class="login-error" id="loginError">Username atau password salah. Silakan coba lagi.</div>

    <label class="login-label" for="loginUser">Username</label>
    <input class="login-input" type="text" id="loginUser" placeholder="Masukkan username" autocomplete="username" onkeydown="if(event.key==='Enter')doLogin()">

    <label class="login-label" for="loginPass">Password</label>
    <div class="login-pw-wrap">
      <input class="login-input" type="password" id="loginPass" placeholder="Masukkan password" autocomplete="current-password" onkeydown="if(event.key==='Enter')doLogin()">
      <button class="toggle-pw" onclick="togglePw()" title="Tampilkan/sembunyikan password">&#128065;</button>
    </div>

    <button class="login-btn" id="loginBtn" onclick="doLogin()">Masuk</button>

    <div class="login-hint">
      <strong>Akun tersedia:</strong><br>
      Admin &mdash; user: <strong>admin</strong> / pass: <strong>opname2026</strong><br>
      Petugas &mdash; user: <strong>roxi</strong> / pass: <strong>roxi2026</strong><br>
      Manajemen &mdash; user: <strong>manager</strong> / pass: <strong>bri2026</strong>
    </div>

    <div class="login-footer">Dashboard Opname Inventori &mdash; Konfidensial &mdash; 2026</div>
  </div>
</div>

<div class="app" id="mainApp" style="display:none">

<!-- SIDEBAR -->
<div class="sidebar">
  <div class="sidebar-logo">
    <div class="logo-mark"><span>BRI</span></div>
    <div class="logo-name">Opname Inventori Kartu ATM</div>
    <div class="logo-sub">Sistem Manajemen Opname</div>
  </div>
  <nav class="nav">
    <div class="nav-section">Menu utama</div>
    <a class="nav-item active" onclick="gotoPage('ringkasan',this)" href="#">
      <svg class="nav-icon" viewBox="0 0 16 16" fill="none"><rect x="1" y="1" width="6" height="6" rx="1.5" fill="currentColor" opacity=".9"/><rect x="9" y="1" width="6" height="6" rx="1.5" fill="currentColor" opacity=".9"/><rect x="1" y="9" width="6" height="6" rx="1.5" fill="currentColor" opacity=".4"/><rect x="9" y="9" width="6" height="6" rx="1.5" fill="currentColor" opacity=".4"/></svg>
      Ringkasan
    </a>
    <a class="nav-item" onclick="gotoPage('rekon',this)" href="#">
      <svg class="nav-icon" viewBox="0 0 16 16" fill="none"><path d="M2 4h12M2 8h8M2 12h10" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
      Rekonsiliasi
    </a>
    <a class="nav-item" onclick="gotoPage('kartu',this)" href="#">
      <svg class="nav-icon" viewBox="0 0 16 16" fill="none"><rect x="1" y="3" width="14" height="10" rx="2" stroke="currentColor" stroke-width="1.3"/><path d="M1 6h14" stroke="currentColor" stroke-width="1.3"/></svg>
      Detail Kartu
    </a>
    <a class="nav-item" onclick="gotoPage('analitik',this)" href="#">
      <svg class="nav-icon" viewBox="0 0 16 16" fill="none"><path d="M2 14L6 9l3 3 3-4 2-2" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
      Analitik
    </a>
    <div class="nav-section">Laporan</div>
    <a class="nav-item" onclick="window.print()" href="#">
      <svg class="nav-icon" viewBox="0 0 16 16" fill="none"><path d="M4 4V2h8v2M3 4h10a1 1 0 011 1v5H2V5a1 1 0 011-1zM4 10v4h8v-4" stroke="currentColor" stroke-width="1.3" stroke-linejoin="round"/></svg>
      Cetak / Print
    </a>
  </nav>
  <div class="sidebar-footer">
    <div class="user-row">
      <div class="avatar">RH</div>
      <div>
        <div class="user-name">Rudi Hermawan</div>
        <div class="user-role">Petugas Opname · NIP003</div>
      </div>
    </div>
  </div>
</div>

<!-- MAIN -->
<div class="main">
  <div class="topbar">
    <div>
      <div class="topbar-title" id="pageTitle">Ringkasan Eksekutif</div>
      <div class="topbar-meta">Cabang Roxi &nbsp;·&nbsp; Supervisor: Dewi Kusuma &nbsp;·&nbsp; Sumber: Roxi_30-3-26_asli</div>
    </div>
    <div class="topbar-right">
      <span class="badge badge-date">30 Maret 2026</span>
      <span class="badge badge-approved">&#10003; Disetujui</span>
      <button class="btn-logout" onclick="doLogout()">&#9654; Keluar</button>
    </div>
  </div>

  <div class="content">

    <!-- ======== PAGE: RINGKASAN ======== -->
    <div id="page-ringkasan" class="page active">
      <div class="kpi-row">
        <div class="kpi"><div class="kpi-label">Total jenis kartu</div><div class="kpi-val blue">30</div><div class="kpi-sub">3 kategori: Chip, Contactless, Mag. Stripe</div></div>
        <div class="kpi"><div class="kpi-label">Total stok WBS</div><div class="kpi-val blue">9.215</div><div class="kpi-sub">Data Card Inquiry sistem</div></div>
        <div class="kpi"><div class="kpi-label">Jenis ada selisih</div><div class="kpi-val red">15</div><div class="kpi-sub">dari 30 total jenis kartu</div></div>
        <div class="kpi"><div class="kpi-label">Tingkat akurasi</div><div class="kpi-val amber">50%</div><div class="kpi-sub">15 dari 30 jenis cocok WBS</div></div>
      </div>

      <div style="margin-bottom:18px">
        <div class="alert alert-red">
          <div class="alert-icon alert-icon-red">!</div>
          <div><div class="alert-title alert-title-red">Britama Black — selisih kritis &minus;3.254 kartu</div><div class="alert-body alert-body-red">Stok WBS 3.254 kartu namun data fisik tidak tercatat sama sekali. Membutuhkan investigasi dan update Card Inquiry segera.</div></div>
        </div>
        <div class="alert alert-amber">
          <div class="alert-icon alert-icon-amber">!</div>
          <div><div class="alert-title alert-title-amber">3 jenis kartu tidak memiliki data fisik tercatat</div><div class="alert-body alert-body-amber">GPN Simpedes (149), Britama Bisnis (68), Britama Valas (44) &mdash; total 261 kartu WBS tanpa data fisik. Perlu verifikasi lapangan.</div></div>
        </div>
      </div>

      <div class="grid2">
        <div class="card">
          <div class="card-hdr"><div class="card-title">Stok WBS vs kartu fisik per jenis (chip)</div></div>
          <div class="leg">
            <span class="leg-i"><span class="leg-sq" style="background:#003087"></span>Stok WBS</span>
            <span class="leg-i"><span class="leg-sq" style="background:#66bb6a"></span>Kartu fisik</span>
          </div>
          <div class="chart-box" style="height:270px"><canvas id="cBarMain" role="img" aria-label="Bar chart stok WBS vs fisik per jenis kartu chip.">Perbandingan stok dan fisik per jenis kartu chip.</canvas></div>
        </div>
        <div class="card">
          <div class="card-hdr"><div class="card-title">Status rekonsiliasi keseluruhan</div></div>
          <div class="chart-box" style="height:160px"><canvas id="cDonut" role="img" aria-label="15 cocok dan 15 selisih dari 30 jenis kartu.">15 cocok, 15 selisih.</canvas></div>
          <div class="leg" style="margin-top:10px;justify-content:center">
            <span class="leg-i"><span class="leg-sq" style="background:#43a047"></span>Cocok / Sama &mdash; 15</span>
            <span class="leg-i"><span class="leg-sq" style="background:#e53935"></span>Selisih &mdash; 15</span>
          </div>
          <div style="margin-top:16px">
            <div class="pb-row"><div class="pb-hdr"><span>Chip (26 jenis)</span><span style="color:#e65100;font-weight:600">50%</span></div><div class="pb-track"><div class="pb-fill" style="width:50%;background:#1565c0"></div></div></div>
            <div class="pb-row"><div class="pb-hdr"><span>Contactless (1 jenis)</span><span style="color:#c62828;font-weight:600">Selisih</span></div><div class="pb-track"><div class="pb-fill" style="width:15%;background:#e53935"></div></div></div>
            <div class="pb-row"><div class="pb-hdr"><span>Magnetic stripe (2 jenis)</span><span style="color:#e65100;font-weight:600">50%</span></div><div class="pb-track"><div class="pb-fill" style="width:50%;background:#ef6c00"></div></div></div>
          </div>
        </div>
      </div>

      <div class="grid3">
        <div class="card">
          <div class="card-hdr"><div class="card-title">Top 5 selisih terbesar</div></div>
          <div class="chart-box" style="height:190px"><canvas id="cTop5" role="img" aria-label="5 jenis kartu dengan selisih stok terbesar.">Top 5 selisih kartu.</canvas></div>
        </div>
        <div class="card">
          <div class="card-hdr"><div class="card-title">Distribusi stok per kategori</div></div>
          <div class="chart-box" style="height:190px"><canvas id="cPieCat" role="img" aria-label="Distribusi stok per kategori kartu.">Distribusi per kategori.</canvas></div>
        </div>
        <div class="card">
          <div class="card-hdr"><div class="card-title">Akurasi per kategori (%)</div></div>
          <div class="chart-box" style="height:190px"><canvas id="cAkurasi" role="img" aria-label="Tingkat akurasi per kategori kartu dalam persen.">Akurasi per kategori.</canvas></div>
        </div>
      </div>

      <div class="page-footer">
        <div class="footer-left">Dashboard Opname Inventori Kartu ATM &mdash; Cabang Roxi &mdash; 30 Maret 2026 &mdash; Konfidensial</div>
        <div class="footer-right">
          <button class="btn-export" onclick="window.print()">&#128438; Cetak Halaman</button>
        </div>
      </div>
    </div>

    <!-- ======== PAGE: REKONSILIASI ======== -->
    <div id="page-rekon" class="page">
      <div class="kpi-row">
        <div class="kpi"><div class="kpi-label">Jenis cocok (Sama)</div><div class="kpi-val green">15</div><div class="kpi-sub">dari 30 total jenis kartu</div></div>
        <div class="kpi"><div class="kpi-label">Jenis selisih</div><div class="kpi-val red">15</div><div class="kpi-sub">perlu tindak lanjut</div></div>
        <div class="kpi"><div class="kpi-label">Total stok WBS</div><div class="kpi-val blue">9.215</div><div class="kpi-sub">sistem Card Inquiry</div></div>
        <div class="kpi"><div class="kpi-label">Tingkat akurasi</div><div class="kpi-val amber">50%</div><div class="kpi-sub">berbasis cocok WBS</div></div>
      </div>

      <div class="sec-sep">Chip &mdash; 26 jenis kartu</div>
      <div class="card" style="padding:0;margin-bottom:18px">
        <div class="tbl-scroll">
          <table>
            <thead><tr><th style="width:36px">#</th><th>Nama kartu</th><th style="text-align:right;width:90px">Stok WBS</th><th style="text-align:right;width:90px">Kartu fisik</th><th style="text-align:right;width:80px">Selisih</th><th style="width:90px">Status</th></tr></thead>
            <tbody id="tRekon"></tbody>
          </table>
        </div>
      </div>

      <div class="grid2b">
        <div class="card">
          <div class="card-hdr"><div class="card-title">Contactless</div></div>
          <table>
            <thead><tr><th>Nama kartu</th><th style="text-align:right">WBS</th><th style="text-align:right">Fisik</th><th style="text-align:right">Selisih</th><th>Status</th></tr></thead>
            <tbody>
              <tr><td>Britama Black CL (set 1)</td><td style="text-align:right">70</td><td style="text-align:right">70</td><td style="text-align:right;color:#2e7d32;font-weight:600">0</td><td><span class="pill-ok"><span class="dot dot-g"></span>Sama</span></td></tr>
              <tr><td>Britama Black CL (set 2)</td><td style="text-align:right">743</td><td style="text-align:right">76</td><td style="text-align:right;color:#c62828;font-weight:600">+667</td><td><span class="pill-err"><span class="dot dot-r"></span>Selisih</span></td></tr>
            </tbody>
          </table>
        </div>
        <div class="card">
          <div class="card-hdr"><div class="card-title">Magnetic stripe</div></div>
          <table>
            <thead><tr><th>Nama kartu</th><th style="text-align:right">WBS</th><th style="text-align:right">Fisik</th><th style="text-align:right">Selisih</th><th>Status</th></tr></thead>
            <tbody>
              <tr><td>KIP Kemendikbud (set 1)</td><td style="text-align:right">117</td><td style="text-align:right">117</td><td style="text-align:right;color:#2e7d32;font-weight:600">0</td><td><span class="pill-ok"><span class="dot dot-g"></span>Sama</span></td></tr>
              <tr><td>KIP Kemendikbud (set 2)</td><td style="text-align:right">758</td><td style="text-align:right">326</td><td style="text-align:right;color:#c62828;font-weight:600">+432</td><td><span class="pill-err"><span class="dot dot-r"></span>Selisih</span></td></tr>
              <tr><td>Kartu Bansos</td><td style="text-align:right">—</td><td style="text-align:right">—</td><td style="text-align:right;color:#aaa">—</td><td><span style="font-size:11px;color:#aaa">—</span></td></tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="card" style="margin-bottom:18px">
        <div class="card-hdr"><div class="card-title">Perbandingan WBS vs fisik per jenis (chip)</div></div>
        <div class="leg">
          <span class="leg-i"><span class="leg-sq" style="background:#003087"></span>Stok WBS</span>
          <span class="leg-i"><span class="leg-sq" style="background:#66bb6a"></span>Kartu fisik</span>
        </div>
        <div class="chart-box" style="height:260px"><canvas id="cRekonBar" role="img" aria-label="Perbandingan stok WBS dan fisik per jenis kartu chip.">WBS vs fisik per jenis.</canvas></div>
      </div>

      <div class="page-footer">
        <div class="footer-left">Dashboard Opname Inventori Kartu ATM &mdash; Cabang Roxi &mdash; 30 Maret 2026 &mdash; Konfidensial</div>
        <div class="footer-right"><button class="btn-export" onclick="window.print()">&#128438; Cetak</button></div>
      </div>
    </div>

    <!-- ======== PAGE: DETAIL KARTU ======== -->
    <div id="page-kartu" class="page">
      <div class="kpi-row">
        <div class="kpi"><div class="kpi-label">Total jenis</div><div class="kpi-val blue">30</div></div>
        <div class="kpi"><div class="kpi-label">Total stok WBS</div><div class="kpi-val blue">9.215</div></div>
        <div class="kpi"><div class="kpi-label">Jenis cocok</div><div class="kpi-val green">15</div></div>
        <div class="kpi"><div class="kpi-label">Jenis selisih</div><div class="kpi-val red">15</div></div>
      </div>
      <div class="card">
        <div class="filter-row" id="kartuFilter">
          <button class="fbtn on" onclick="filterKartu('Semua',this)">Semua (30)</button>
          <button class="fbtn" onclick="filterKartu('Sama',this)">Cocok (15)</button>
          <button class="fbtn" onclick="filterKartu('Selisih',this)">Selisih (15)</button>
          <button class="fbtn" onclick="filterKartu('Chip',this)">Chip (26)</button>
          <button class="fbtn" onclick="filterKartu('Contactless',this)">Contactless (1)</button>
          <button class="fbtn" onclick="filterKartu('Magnetic',this)">Magnetic stripe (3)</button>
        </div>
        <div class="tbl-wrap">
          <div class="tbl-scroll">
            <table>
              <thead><tr><th style="width:36px">#</th><th>Nama kartu</th><th style="width:110px">Kategori</th><th style="text-align:right;width:90px">Stok WBS</th><th style="text-align:right;width:90px">Fisik</th><th style="text-align:right;width:80px">Selisih</th><th style="width:90px">Status</th></tr></thead>
              <tbody id="tKartu"></tbody>
            </table>
          </div>
        </div>
      </div>
      <div class="page-footer">
        <div class="footer-left">Dashboard Opname Inventori Kartu ATM &mdash; Cabang Roxi &mdash; 30 Maret 2026 &mdash; Konfidensial</div>
        <div class="footer-right"><button class="btn-export" onclick="window.print()">&#128438; Cetak</button></div>
      </div>
    </div>

    <!-- ======== PAGE: ANALITIK ======== -->
    <div id="page-analitik" class="page">
      <div class="kpi-row">
        <div class="kpi"><div class="kpi-label">Stok terbesar</div><div class="kpi-val blue">3.254</div><div class="kpi-sub">Britama Black</div></div>
        <div class="kpi"><div class="kpi-label">Selisih terbesar</div><div class="kpi-val red">&minus;3.254</div><div class="kpi-sub">Britama Black</div></div>
        <div class="kpi"><div class="kpi-label">Akurasi chip</div><div class="kpi-val amber">50%</div><div class="kpi-sub">13 dari 26 jenis</div></div>
        <div class="kpi"><div class="kpi-label">Akurasi keseluruhan</div><div class="kpi-val amber">50%</div><div class="kpi-sub">15 dari 30 jenis</div></div>
      </div>
      <div class="grid2b" style="margin-bottom:18px">
        <div class="card">
          <div class="card-hdr"><div class="card-title">Selisih per jenis kartu chip</div></div>
          <div class="chart-box" style="height:310px"><canvas id="cSelisih" role="img" aria-label="Bar chart selisih stok per jenis kartu chip. Merah = kekurangan, hijau = sesuai, kuning = lebih.">Selisih per kartu.</canvas></div>
        </div>
        <div class="card">
          <div class="card-hdr"><div class="card-title">10 jenis kartu dengan stok terbesar</div></div>
          <div class="chart-box" style="height:310px"><canvas id="cTop10" role="img" aria-label="10 jenis kartu dengan stok terbesar.">10 stok terbesar.</canvas></div>
        </div>
      </div>
      <div class="card">
        <div class="card-hdr"><div class="card-title">Perbandingan WBS vs fisik tercatat per kategori</div></div>
        <div class="leg">
          <span class="leg-i"><span class="leg-sq" style="background:#003087"></span>Stok WBS</span>
          <span class="leg-i"><span class="leg-sq" style="background:#66bb6a"></span>Fisik tercatat</span>
        </div>
        <div class="chart-box" style="height:180px"><canvas id="cKatComp" role="img" aria-label="Perbandingan WBS dan fisik tercatat per kategori kartu.">WBS vs fisik per kategori.</canvas></div>
      </div>
      <div class="page-footer">
        <div class="footer-left">Dashboard Opname Inventori Kartu ATM &mdash; Cabang Roxi &mdash; 30 Maret 2026 &mdash; Konfidensial</div>
        <div class="footer-right"><button class="btn-export" onclick="window.print()">&#128438; Cetak</button></div>
      </div>
    </div>

  </div>
</div>
</div>
</div>

<script>
const USERS={
  admin:  {pass:'opname2026', name:'Administrator',  role:'Admin Sistem'},
  roxi:   {pass:'roxi2026',   name:'Rudi Hermawan',  role:'Petugas Opname · NIP003'},
  manager:{pass:'bri2026',    name:'Dewi Kusuma',    role:'Supervisor / Manajemen'},
};

function doLogin(){
  const u=document.getElementById('loginUser').value.trim().toLowerCase();
  const p=document.getElementById('loginPass').value;
  const err=document.getElementById('loginError');
  const inp=document.getElementById('loginUser');
  const inpP=document.getElementById('loginPass');
  if(USERS[u]&&USERS[u].pass===p){
    err.classList.remove('show');
    inp.classList.remove('err');
    inpP.classList.remove('err');
    sessionStorage.setItem('briAuth',u);
    document.getElementById('loginScreen').classList.add('hidden');
    document.getElementById('mainApp').style.display='flex';
    const usr=USERS[u];
    document.querySelector('.user-name').textContent=usr.name;
    document.querySelector('.user-role').textContent=usr.role;
    const initials=usr.name.split(' ').map(w=>w[0]).slice(0,2).join('').toUpperCase();
    document.querySelector('.avatar').textContent=initials;
  } else {
    err.classList.add('show');
    inp.classList.add('err');
    inpP.classList.add('err');
    inpP.value='';
    inpP.focus();
  }
}

function doLogout(){
  sessionStorage.removeItem('briAuth');
  document.getElementById('mainApp').style.display='none';
  document.getElementById('loginScreen').classList.remove('hidden');
  document.getElementById('loginUser').value='';
  document.getElementById('loginPass').value='';
  document.getElementById('loginError').classList.remove('show');
  document.getElementById('loginUser').classList.remove('err');
  document.getElementById('loginPass').classList.remove('err');
  document.getElementById('loginUser').focus();
}

function togglePw(){
  const inp=document.getElementById('loginPass');
  inp.type=inp.type==='password'?'text':'password';
}

(function(){
  const s=sessionStorage.getItem('briAuth');
  if(s&&USERS[s]){
    document.getElementById('loginScreen').classList.add('hidden');
    document.getElementById('mainApp').style.display='flex';
    const usr=USERS[s];
    document.querySelector('.user-name').textContent=usr.name;
    document.querySelector('.user-role').textContent=usr.role;
    const initials=usr.name.split(' ').map(w=>w[0]).slice(0,2).join('').toUpperCase();
    document.querySelector('.avatar').textContent=initials;
  }
})();

const pageTitles={ringkasan:'Ringkasan Eksekutif',rekon:'Rekonsiliasi WBS vs Fisik',kartu:'Detail Kartu',analitik:'Analitik & Visualisasi'};
function gotoPage(id,el){
  event.preventDefault();
  document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(n=>n.classList.remove('active'));
  document.getElementById('page-'+id).classList.add('active');
  el.classList.add('active');
  document.getElementById('pageTitle').textContent=pageTitles[id];
}

const cards=[
  {no:1,nama:'Cobranding Wisata Nusantara',kat:'Chip',stok:183,fisik:183,selisih:0,ket:'Sama'},
  {no:2,nama:'Wisata Nusantara Bunaken',kat:'Chip',stok:170,fisik:170,selisih:0,ket:'Sama'},
  {no:3,nama:'Wisata Nusantara Labuan Bajo',kat:'Chip',stok:180,fisik:180,selisih:0,ket:'Sama'},
  {no:4,nama:'Britama Silver',kat:'Chip',stok:15,fisik:null,selisih:-15,ket:'Sesilih'},
  {no:5,nama:'Wisata Nusantara Ranukumbolo',kat:'Chip',stok:183,fisik:183,selisih:0,ket:'Sama'},
  {no:6,nama:'Debit Series Basket',kat:'Chip',stok:312,fisik:258,selisih:-54,ket:'Sama'},
  {no:7,nama:'Debit Series Gentlemen',kat:'Chip',stok:112,fisik:100,selisih:-12,ket:'Sama'},
  {no:8,nama:'Britama Black',kat:'Chip',stok:3254,fisik:null,selisih:-3254,ket:'Sesilih'},
  {no:9,nama:'Giro Individual Classic',kat:'Chip',stok:113,fisik:100,selisih:-13,ket:'Sesilih'},
  {no:10,nama:'Giro Individual Gold',kat:'Chip',stok:128,fisik:115,selisih:13,ket:'Selisih'},
  {no:11,nama:'Giro Individual Platinum',kat:'Chip',stok:129,fisik:129,selisih:0,ket:'Sama'},
  {no:12,nama:'Giro Badan Usaha Classic',kat:'Chip',stok:112,fisik:112,selisih:0,ket:'Sama'},
  {no:13,nama:'Giro Badan Usaha Gold',kat:'Chip',stok:107,fisik:88,selisih:-19,ket:'Sesilih'},
  {no:14,nama:'Giro Badan Usaha Platinum',kat:'Chip',stok:118,fisik:117,selisih:1,ket:'Selisih'},
  {no:15,nama:'Britama Bisnis',kat:'Chip',stok:68,fisik:null,selisih:-68,ket:'Sesilih'},
  {no:16,nama:'Britama Valas',kat:'Chip',stok:44,fisik:null,selisih:-44,ket:'Sesilih'},
  {no:17,nama:'GPN Simpedes',kat:'Chip',stok:149,fisik:null,selisih:-149,ket:'Sesilih'},
  {no:18,nama:'GPN Britama X',kat:'Chip',stok:160,fisik:null,selisih:null,ket:'Sesilih'},
  {no:19,nama:'GPN Junio Beruang',kat:'Chip',stok:44,fisik:null,selisih:-44,ket:'Sama'},
  {no:20,nama:'GPN Junio Camera',kat:'Chip',stok:100,fisik:100,selisih:0,ket:'Sesilih'},
  {no:21,nama:'NTL Green Venhicle',kat:'Chip',stok:7,fisik:7,selisih:0,ket:'Sama'},
  {no:22,nama:'NTL Green Earth',kat:'Chip',stok:640,fisik:620,selisih:-20,ket:'Sesilih'},
  {no:23,nama:'NTL Hardthirteen',kat:'Chip',stok:639,fisik:639,selisih:0,ket:'Sama'},
  {no:24,nama:'NTL Authentic Fauna',kat:'Chip',stok:637,fisik:628,selisih:-9,ket:'Sama'},
  {no:25,nama:'NTL Cycling New',kat:'Chip',stok:635,fisik:635,selisih:0,ket:'Sama'},
  {no:26,nama:'Cashcard Chip',kat:'Chip',stok:73,fisik:50,selisih:-23,ket:'Sama'},
  {no:27,nama:'Britama Black CL',kat:'Contactless',stok:743,fisik:76,selisih:667,ket:'Selisih'},
  {no:28,nama:'KIP Kemendikbud (set 1)',kat:'Magnetic',stok:117,fisik:117,selisih:0,ket:'Sama'},
  {no:29,nama:'KIP Kemendikbud (set 2)',kat:'Magnetic',stok:758,fisik:326,selisih:432,ket:'Selisih'},
  {no:30,nama:'Kartu Bansos',kat:'Magnetic',stok:null,fisik:null,selisih:null,ket:'—'},
];

function fv(v){return v!=null?v.toLocaleString('id-ID'):'—'}
function fs(v){
  if(v==null) return '<span style="color:#aaa">—</span>';
  if(v===0) return '<span style="color:#2e7d32;font-weight:600">0</span>';
  const c=v<0?'#c62828':'#e65100';
  return `<span style="color:${c};font-weight:600">${v>0?'+':''}${v.toLocaleString('id-ID')}</span>`;
}
function pill(k){
  if(k==='Sama') return `<span class="pill-ok"><span class="dot dot-g"></span>Sama</span>`;
  if(k==='—') return `<span style="color:#aaa;font-size:12px">—</span>`;
  return `<span class="pill-err"><span class="dot dot-r"></span>${k}</span>`;
}
function katPill(k){
  if(k==='Chip') return `<span class="pill-chip">Chip</span>`;
  if(k==='Contactless') return `<span class="pill-cl">Contactless</span>`;
  return `<span class="pill-mag">Magnetic</span>`;
}

function renderRekon(){
  const chip=cards.filter(d=>d.kat==='Chip');
  document.getElementById('tRekon').innerHTML=chip.map(d=>`<tr>
    <td style="color:#aaa">${d.no}</td><td>${d.nama}</td>
    <td style="text-align:right">${fv(d.stok)}</td>
    <td style="text-align:right">${fv(d.fisik)}</td>
    <td style="text-align:right">${fs(d.selisih)}</td>
    <td>${pill(d.ket)}</td>
  </tr>`).join('');
}

function renderKartu(filter){
  let rows=filter==='Semua'?cards:
    filter==='Sama'?cards.filter(d=>d.ket==='Sama'):
    filter==='Selisih'?cards.filter(d=>d.ket!=='Sama'&&d.ket!=='—'):
    filter==='Chip'?cards.filter(d=>d.kat==='Chip'):
    filter==='Contactless'?cards.filter(d=>d.kat==='Contactless'):
    cards.filter(d=>d.kat==='Magnetic');
  document.getElementById('tKartu').innerHTML=rows.map(d=>`<tr>
    <td style="color:#aaa">${d.no}</td><td>${d.nama}</td>
    <td>${katPill(d.kat)}</td>
    <td style="text-align:right">${fv(d.stok)}</td>
    <td style="text-align:right">${fv(d.fisik)}</td>
    <td style="text-align:right">${fs(d.selisih)}</td>
    <td>${pill(d.ket)}</td>
  </tr>`).join('');
}

function filterKartu(f,btn){
  document.querySelectorAll('#kartuFilter .fbtn').forEach(b=>b.classList.remove('on'));
  btn.classList.add('on');
  renderKartu(f);
}

renderRekon();
renderKartu('Semua');

const cLabels=['WN Cobrand','WN Bunaken','WN Labuan','Br.Silver','WN Ranuku','Dbt Basket','Dbt Gentlm','Br.Black','Giro IC','Giro IG','Giro IP','Giro BUC','Giro BUG','Giro BUP','Br.Bisnis','Br.Valas','GPN Simp','GPN BrX','GPN Junio B','GPN Junio C','NTL GrnVhc','NTL GrnEth','NTL Hard13','NTL Fauna','NTL Cycling','Cashcard'];
const cStok=[183,170,180,15,183,312,112,3254,113,128,129,112,107,118,68,44,149,160,44,100,7,640,639,637,635,73];
const cFisik=[183,170,180,0,183,258,100,0,100,115,129,112,88,117,0,0,0,0,0,100,7,620,639,628,635,50];
const cSel=[0,0,0,-15,0,-54,-12,-3254,-13,13,0,0,-19,1,-68,-44,-149,0,-44,0,0,-20,0,-9,0,-23];

new Chart(document.getElementById('cBarMain'),{type:'bar',data:{labels:cLabels,datasets:[
  {label:'Stok WBS',data:cStok,backgroundColor:'#003087',borderRadius:2},
  {label:'Kartu fisik',data:cFisik,backgroundColor:'#66bb6a',borderRadius:2}
]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:{grid:{display:false},ticks:{font:{size:9},maxRotation:55}},y:{grid:{color:'rgba(0,0,0,.06)'},ticks:{font:{size:10}}}}}});

new Chart(document.getElementById('cDonut'),{type:'doughnut',data:{labels:['Cocok','Selisih'],datasets:[{data:[15,15],backgroundColor:['#43a047','#e53935'],borderWidth:2,borderColor:'#fff',hoverOffset:5}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},cutout:'68%'}});

new Chart(document.getElementById('cTop5'),{type:'bar',data:{labels:['Br. Black','GPN Simpedes','Br. Bisnis','Br. Valas','NTL Grn Earth'],datasets:[{data:[-3254,-149,-68,-44,-20],backgroundColor:['#b71c1c','#e53935','#ef9a9a','#ef9a9a','#ffcdd2'],borderRadius:4}]},options:{indexAxis:'y',responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:{grid:{color:'rgba(0,0,0,.06)'},ticks:{font:{size:10}}},y:{grid:{display:false},ticks:{font:{size:10}}}}}});

new Chart(document.getElementById('cPieCat'),{type:'doughnut',data:{labels:['Chip 8.312','Mag. Stripe 875','Contactless 743'],datasets:[{data:[8312,875,743],backgroundColor:['#003087','#66bb6a','#ef6c00'],borderWidth:2,borderColor:'#fff'}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{position:'bottom',labels:{font:{size:11},boxWidth:12,padding:10}}}}});

new Chart(document.getElementById('cAkurasi'),{type:'bar',data:{labels:['Chip','Contactless','Mag. Stripe','Total'],datasets:[{data:[50,50,50,50],backgroundColor:['#003087','#ef6c00','#43a047','#1565c0'],borderRadius:6}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false},tooltip:{callbacks:{label:v=>`${v.raw}%`}}},scales:{x:{grid:{display:false},ticks:{font:{size:11}}},y:{max:100,grid:{color:'rgba(0,0,0,.06)'},ticks:{font:{size:10},callback:v=>`${v}%`}}}}});

new Chart(document.getElementById('cRekonBar'),{type:'bar',data:{labels:cLabels,datasets:[
  {label:'Stok WBS',data:cStok,backgroundColor:'#003087',borderRadius:2},
  {label:'Kartu fisik',data:cFisik,backgroundColor:'#66bb6a',borderRadius:2}
]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:{grid:{display:false},ticks:{font:{size:9},maxRotation:55}},y:{grid:{color:'rgba(0,0,0,.06)'},ticks:{font:{size:10}}}}}});

new Chart(document.getElementById('cSelisih'),{type:'bar',data:{labels:cLabels,datasets:[{data:cSel,backgroundColor:cSel.map(v=>v===0?'#43a047':v<0?'#e53935':'#ef6c00'),borderRadius:3}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:{grid:{display:false},ticks:{font:{size:9},maxRotation:55}},y:{grid:{color:'rgba(0,0,0,.06)'},ticks:{font:{size:10}}}}}});

new Chart(document.getElementById('cTop10'),{type:'bar',data:{labels:['Br.Black','NTL GrnEth','NTL Hard13','NTL Fauna','NTL Cycling','WN Cobrand','WN Ranuku','WN Labuan','Dbt Basket','WN Bunaken'],datasets:[{data:[3254,640,639,637,635,183,183,180,312,170],backgroundColor:'#003087',borderRadius:4}]},options:{indexAxis:'y',responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:{grid:{color:'rgba(0,0,0,.06)'},ticks:{font:{size:10}}},y:{grid:{display:false},ticks:{font:{size:10}}}}}});

new Chart(document.getElementById('cKatComp'),{type:'bar',data:{labels:['Chip','Contactless','Magnetic stripe'],datasets:[
  {label:'Stok WBS',data:[8312,743,875],backgroundColor:'#003087',borderRadius:3},
  {label:'Fisik tercatat',data:[3635,76,443],backgroundColor:'#66bb6a',borderRadius:3}
]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:{grid:{display:false},ticks:{font:{size:12}}},y:{grid:{color:'rgba(0,0,0,.06)'},ticks:{font:{size:10}}}}}});
</script>
</body>
</html>
