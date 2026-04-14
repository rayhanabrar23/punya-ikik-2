import streamlit as st
import pandas as pd
import plotly.express as px

# Konfigurasi Halaman
st.set_page_config(page_title="Opname Inventori Kartu ATM", layout="wide")

# Styling CSS untuk mempercantik tampilan
st.markdown("""
    <style>
    .main { background-color: #f4f6f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #e8eaf0; }
    </style>
    """, unsafe_allow_html=True)

st.title("📊 Dashboard Opname Inventori Kartu ATM")
st.subheader("Cabang Roxi — Sistem Manajemen Opname")

# 1. FITUR UPLOADER
uploaded_file = st.file_uploader("Upload File Excel Inventori", type=["xlsx", "xls"])

if uploaded_file:
    # Membaca Data
    df = pd.read_excel(uploaded_file)
    
    # Bersihkan nama kolom (menghapus spasi berlebih)
    df.columns = df.columns.str.strip()
    
    # 2. PENGOLAHAN DATA (PANDAS)
    # Hitung Selisih
    df['SELISIH'] = df['FISIK'] - df['STOK']
    
    # Tentukan Status
    df['STATUS'] = df['SELISIH'].apply(lambda x: "SAMA" if x == 0 else "SELISIH")
    
    # Logika Kategori Otomatis (Karena di Excel tidak ada)
    def tentukan_kategori(nama):
        nama = str(nama).upper()
        if "BRITAMA" in nama or "DEBIT" in nama: return "CHIP"
        if "WISATA" in nama: return "MAGNETIC STRIPE"
        if "GIRO" in nama: return "BUSINESS"
        return "LAINNYA"
    
    df['KATEGORI'] = df['NAMA KARTU'].apply(tentukan_kategori)

    # 3. BAGIAN KPI (METRICS)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Jenis Kartu", len(df))
    with col2:
        st.metric("Total Stok (Sistem)", f"{int(df['STOK'].sum()):,}")
    with col3:
        total_selisih = len(df[df['STATUS'] == "SELISIH"])
        st.metric("Jenis Ada Selisih", total_selisih, delta=f"{total_selisih} jenis", delta_color="inverse")
    with col4:
        akurasi = (len(df[df['STATUS'] == "SAMA"]) / len(df)) * 100
        st.metric("Tingkat Akurasi", f"{akurasi:.1f}%")

    st.divider()

    # 4. VISUALISASI
    left_col, right_col = st.columns([2, 1])

    with left_col:
        st.write("### Perbandingan Stok vs Fisik")
        # Grafik batang interaktif menggunakan Plotly
        fig_bar = px.bar(df, x='NAMA KARTU', y=['STOK', 'FISIK'], 
                         barmode='group',
                         labels={'value': 'Jumlah Kartu', 'variable': 'Tipe'},
                         color_discrete_map={'STOK': '#003087', 'FISIK': '#66bb6a'})
        st.plotly_chart(fig_bar, use_container_width=True)

    with right_col:
        st.write("### Proporsi Akurasi")
        fig_pie = px.pie(df, names='STATUS', 
                         color='STATUS',
                         color_discrete_map={'SAMA': '#43a047', 'SELISIH': '#e53935'},
                         hole=0.4)
        st.plotly_chart(fig_pie, use_container_width=True)

    # 5. TABEL DETAIL
    st.write("### Detail Rekonsiliasi Data")
    
    # Filter sederhana
    status_filter = st.multiselect("Filter Status:", options=df['STATUS'].unique(), default=df['STATUS'].unique())
    df_filtered = df[df['STATUS'].isin(status_filter)]

    # Menampilkan tabel dengan highlight warna
    def highlight_selisih(s):
        return ['background-color: #ffcccc' if v != 0 else '' for v in s]

    st.dataframe(
        df_filtered.style.apply(highlight_selisih, subset=['SELISIH']),
        use_container_width=True,
        hide_index=True
    )

    # Tombol Download Hasil Olahan
    st.download_button(
        label="📥 Download Hasil Rekonsiliasi (Excel)",
        data=df.to_csv(index=False).encode('utf-8'),
        file_name='hasil_opname_roxi.csv',
        mime='text/csv',
    )

else:
    st.info("Silakan upload file Excel untuk melihat dashboard.")
    st.image("https://via.placeholder.com/800x400.png?text=Menunggu+Upload+File+Excel...", use_column_width=True)
