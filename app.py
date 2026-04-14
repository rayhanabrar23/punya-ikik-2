import streamlit as st
import streamlit.components.v1 as components

# Mengatur layout Streamlit agar memenuhi layar
st.set_page_config(page_title="Dashboard Opname BRI", layout="wide")

# Seluruh kode HTML/CSS/JS Anda dimasukkan ke dalam variabel html_code
html_code = """
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

/* MAIN CONTENT */
.main{flex:1;display:flex;flex-direction:column;min-width:0}
.topbar{height:56px;background:#fff;border-bottom:1px solid #e8eaf0;display:flex;align-items:center;justify-content:space-between;padding:0 28px;flex-shrink:0;position:sticky;top:0;z-index:10}
.topbar-title{font-size:16px;font-weight:600;color:#1a1a2e}
.content{flex:1;padding:24px 28px}

/* KPI */
.kpi-row{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:22px}
.kpi{background:#fff;border-radius:10px;padding:16px 18px;border:1px solid #e8eaf0}
.kpi-label{font-size:11px;color:#888;text-transform:uppercase;letter-spacing:.05em;margin-bottom:8px;font-weight:500}
.kpi-val{font-size:26px;font-weight:700;line-height:1}
.kpi-val.blue{color:#003087}
.kpi-val.red{color:#c62828}

/* TABLE */
.tbl-wrap{border:1px solid #e8eaf0;border-radius:10px;overflow:hidden;background:#fff}
table{width:100%;border-collapse:collapse;font-size:13px}
th{font-size:11px;font-weight:600;color:#888;text-align:left;padding:10px 12px;border-bottom:1px solid #e8eaf0;background:#fafafa}
td{padding:9px 12px;border-bottom:1px solid #f0f2f5;color:#1a1a2e}
.pill-err{display:inline-flex;align-items:center;color:#c62828;background:#fff5f5;padding:3px 10px;border-radius:20px;font-weight:500}

.card{background:#fff;border:1px solid #e8eaf0;border-radius:12px;padding:18px 20px;margin-bottom:20px}
</style>
</head>
<body>

<div class="app">
    <div class="sidebar">
        <div class="sidebar-logo">
            <div class="logo-mark"><span>BRI</span></div>
            <div class="logo-name">Opname Inventori Kartu ATM</div>
            <div class="logo-sub">Cabang Roxi</div>
        </div>
        <nav class="nav">
            <div class="nav-section">Menu utama</div>
            <a class="nav-item active" href="#">Ringkasan</a>
            <a class="nav-item" href="#">Rekonsiliasi</a>
            <a class="nav-item" href="#">Detail Kartu</a>
        </nav>
    </div>

    <div class="main">
        <div class="topbar">
            <div class="topbar-title">Ringkasan Eksekutif — Maret 2026</div>
        </div>

        <div class="content">
            <div class="kpi-row">
                <div class="kpi"><div class="kpi-label">Total Jenis Kartu</div><div class="kpi-val blue">30</div></div>
                <div class="kpi"><div class="kpi-label">Total Stok WBS</div><div class="kpi-val blue">9.215</div></div>
                <div class="kpi"><div class="kpi-label">Jenis Selisih</div><div class="kpi-val red">15</div></div>
                <div class="kpi"><div class="kpi-label">Akurasi Akurasi</div><div class="kpi-val" style="color:#e65100">50%</div></div>
            </div>

            <div class="card">
                <h3>Daftar Selisih Kritis</h3>
                <div class="tbl-wrap">
                    <table>
                        <thead>
                            <tr>
                                <th>Nama Kartu</th>
                                <th style="text-align:right">Stok WBS</th>
                                <th style="text-align:right">Fisik</th>
                                <th style="text-align:right">Selisih</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Britama Black</td>
                                <td style="text-align:right">3.254</td>
                                <td style="text-align:right">0</td>
                                <td style="text-align:right"><span class="pill-err">-3.254</span></td>
                            </tr>
                            <tr>
                                <td>GPN Simpedes</td>
                                <td style="text-align:right">149</td>
                                <td style="text-align:right">0</td>
                                <td style="text-align:right"><span class="pill-err">-149</span></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <div class="card">
                <h3>Visualisasi Status Rekonsiliasi</h3>
                <div style="height:300px; width:100%;">
                    <canvas id="chartStatus"></canvas>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
    const ctx = document.getElementById('chartStatus').getContext('2d');
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Cocok (Sama)', 'Selisih'],
            datasets: [{
                data: [15, 15],
                backgroundColor: ['#43a047', '#e53935'],
                borderWidth: 1
            }]
        },
        options: {
            responsive: True,
            maintainAspectRatio: false,
            plugins: {
                legend: { position: 'bottom' }
            }
        }
    });
</script>
</body>
</html>
"""

# Render kode HTML ke dalam UI Streamlit
components.html(html_code, height=900, scrolling=True)
