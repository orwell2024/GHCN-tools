# Step 1: Import Necessary Libraries
# ------------------------------------
import pandas as pd
import requests
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import folium
from folium import plugins
from statsmodels.nonparametric.smoothers_lowess import lowess

# Set a nice style for the plots
sns.set_theme(style="whitegrid")

# Step 2: Define the Station Pairs with Coordinates and Baseline
# -------------------------------------------------------------
station_pairs = [
    {
        "legacy_name": "MULESHOE_NTL_WR",
        "legacy_id": "USC00416137",
        "uscrn_name": "MULESHOE_19_S",
        "uscrn_id": "USW00003054",
        "lat": 34.2267, "lon": -102.7233,  # Muleshoe, TX
        "state": "TX"
    },
    {
        "legacy_name": "MAUNA_LOA_SLOPE_OBS_39",
        "legacy_id": "USC00516198",
        "uscrn_name": "MAUNA_LOA_5_NNE",
        "uscrn_id": "USW00021514",
        "lat": 19.5361, "lon": -155.5783,  # Mauna Loa, HI
        "state": "HI"
    },
    {
        "legacy_name": "BLACK_CANYON_COLORADO",
        "legacy_id": "USR0000CBLA",
        "uscrn_name": "MONTROSE_11_ENE",
        "uscrn_id": "USW00003060",
        "lat": 38.4583, "lon": -107.6333,  # Montrose, CO
        "state": "CO"
    },
    {
        "legacy_name": "CRANE_FLAT_LOOKOUT_CALIFORNIA",
        "legacy_id": "USR0000CCRA",
        "uscrn_name": "YOSEMITE_VILLAGE_12_W",
        "uscrn_id": "USW00053150",
        "lat": 37.7167, "lon": -119.7833,  # Yosemite, CA
        "state": "CA"
    },
    {
        "legacy_name": "DUKE_FOREST_NORTH_CAROLINA",
        "legacy_id": "USR0000NDUK",
        "uscrn_name": "DURHAM_11_W",
        "uscrn_id": "USW00003758",
        "lat": 35.9783, "lon": -79.1000,  # Durham, NC
        "state": "NC"
    },
    {
        "legacy_name": "NIWOT",
        "legacy_id": "USS0005J42S",
        "uscrn_name": "BOULDER_14_W",
        "uscrn_id": "USW00094075",
        "lat": 40.0333, "lon": -105.5833,  # Boulder, CO
        "state": "CO"
    },
    {
        "legacy_name": "MERCURY_DESERT_ROCK_AP",
        "legacy_id": "USW00003160",
        "uscrn_name": "MERCURY_3_SSW",
        "uscrn_id": "USW00053136",
        "lat": 36.6233, "lon": -116.0167,  # Mercury, NV
        "state": "NV"
    },
    {
        "legacy_name": "CRAIG_AFB",
        "legacy_id": "USW00013850",
        "uscrn_name": "SELMA_6_SSE",
        "uscrn_id": "USW00063897",
        "lat": 32.3433, "lon": -87.0067,  # Selma, AL
        "state": "AL"
    },
    {
        "legacy_name": "LIMESTONE_LORING_AFB",
        "legacy_id": "USW00014623",
        "uscrn_name": "LIMESTONE_4_NNW",
        "uscrn_id": "USW00094645",
        "lat": 46.9500, "lon": -67.8833,  # Limestone, ME
        "state": "ME"
    },
    {
        "legacy_name": "BLACKVILLE_3_W",
        "legacy_id": "USC00380764",
        "uscrn_name": "BLACKVILLE_3_W",
        "uscrn_id": "USW00063826",
        "lat": 33.3583, "lon": -81.3000,  # Blackville, SC
        "state": "SC"
    },
    {
        "legacy_name": "HOLLY_SPRINGS_4_N",
        "legacy_id": "USC00224173",
        "uscrn_name": "HOLLY_SPRINGS_4_N",
        "uscrn_id": "USW00023803",
        "lat": 35.6667, "lon": -78.8333,  # Holly Springs, NC
        "state": "NC"
    },
    {
        "legacy_name": "STILLWATER_2_W",
        "legacy_id": "USC00348501",
        "uscrn_name": "STILLWATER_2_W",
        "uscrn_id": "USW00053926",
        "lat": 36.1167, "lon": -97.0833,  # Stillwater, OK
        "state": "OK"
    },
]

BASELINE_START = 1960
BASELINE_END = 1980
MIN_BASELINE_YEARS = 15

# Create a directory to store the downloaded data
if not os.path.exists("station_data"):
    os.makedirs("station_data")

# Step 3: Function to Download and Cache Station Data
# ----------------------------------------------------
def get_station_data(station_id):
    """Downloads and caches GHCN-Daily data for a given station ID."""
    filepath = f"station_data/{station_id}.csv"
    if not os.path.exists(filepath):
        print(f"Downloading data for {station_id}...")
        url = f"https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/access/{station_id}.csv"
        try:
            response = requests.get(url)
            response.raise_for_status()
            with open(filepath, "w") as f:
                f.write(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {station_id}: {e}")
            return None
    else:
        print(f"Using cached data for {station_id}.")

    try:
        df = pd.read_csv(
            filepath,
            usecols=["DATE", "TMAX"],
            parse_dates=["DATE"],
            na_values=[" ", ""],
        )
        df["TMAX"] = pd.to_numeric(df["TMAX"], errors="coerce")
        df.dropna(subset=["TMAX"], inplace=True)
        return df
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None

# Step 4: Alternative Baseline Calculation Function
# ------------------------------------------------
def calculate_alternative_baseline(stitched_df, baseline_start, baseline_end):
    """Calculate alternative baseline when standard period isn't available."""
    alternative_periods = [
        (1971, 1990),  # WMO alternative
        (1981, 2010),  # Current WMO standard
        (1951, 1980),  # GISS standard
        (1961, 1990),  # Another common period
    ]
    
    for alt_start, alt_end in alternative_periods:
        alt_period = stitched_df.loc[str(alt_start):str(alt_end)]
        if not alt_period.empty and len(alt_period) >= 60:
            return alt_period["TMAX"].mean(), f"{alt_start}-{alt_end}"
    
    # Use longest available period that's at least 10 years long
    years_available = stitched_df.index.year.unique()
    if len(years_available) >= 10:
        if len(years_available) >= 20:
            start_year = years_available[len(years_available)//2 - 10]
            end_year = years_available[len(years_available)//2 + 9]
            custom_period = stitched_df.loc[str(start_year):str(end_year)]
            return custom_period["TMAX"].mean(), f"{start_year}-{end_year}"
        else:
            return stitched_df["TMAX"].mean(), f"{years_available.min()}-{years_available.max()}"
    
    return None, None

# Step 5: Process All Pairs for Both Approaches
# ---------------------------------------------
inclusive_pairs = []
strict_pairs = []
dropped_pairs = []
all_pair_info = []

for pair in station_pairs:
    print(f"\n--- Processing Pair: {pair['legacy_name']} / {pair['uscrn_name']} ---")

    legacy_df = get_station_data(pair["legacy_id"])
    uscrn_df = get_station_data(pair["uscrn_id"])

    if legacy_df is None or legacy_df.empty:
        print(f"No valid legacy data for {pair['legacy_id']}. Skipping.")
        dropped_pairs.append(f"{pair['legacy_name']} / {pair['uscrn_name']} - No legacy data")
        continue
    
    if uscrn_df is None or uscrn_df.empty:
        print(f"No valid USCRN data for {pair['uscrn_id']}. Using legacy data only.")
        legacy_df["TMAX"] = legacy_df["TMAX"] / 10
        stitched_df = legacy_df
    else:
        # Convert and stitch data
        legacy_df["TMAX"] = legacy_df["TMAX"] / 10
        uscrn_df["TMAX"] = uscrn_df["TMAX"] / 10
        uscrn_start_date = uscrn_df["DATE"].min()
        legacy_chopped = legacy_df[legacy_df["DATE"] < uscrn_start_date].copy()
        stitched_df = pd.concat([legacy_chopped, uscrn_df], ignore_index=True)
        stitched_df.drop_duplicates(subset="DATE", keep="last", inplace=True)

    stitched_df.set_index("DATE", inplace=True)
    
    # Store pair info for map
    pair_info = {
        'name': f"{pair['legacy_name']} / {pair['uscrn_name']}",
        'lat': pair['lat'],
        'lon': pair['lon'],
        'state': pair['state'],
        'data_start': stitched_df.index.min().year,
        'data_end': stitched_df.index.max().year,
        'strict_qualified': False,
        'inclusive_qualified': False
    }
    
    # Check for strict baseline (1960-1980)
    baseline_period = stitched_df.loc[str(BASELINE_START):str(BASELINE_END)]
    baseline_years = baseline_period.index.year.nunique() if not baseline_period.empty else 0
    
    if not baseline_period.empty and baseline_years >= MIN_BASELINE_YEARS:
        # Qualifies for strict approach
        pair_baseline_avg = baseline_period["TMAX"].mean()
        baseline_period_used = f"{BASELINE_START}-{BASELINE_END}"
        
        monthly_avg = stitched_df.resample("M")["TMAX"].mean()
        pair_anomalies = monthly_avg - pair_baseline_avg
        
        strict_pairs.append({
            'pair_name': pair_info['name'],
            'anomalies': pair_anomalies,
            'baseline_temp': pair_baseline_avg,
            'baseline_period': baseline_period_used,
            'baseline_years': baseline_years,
            'data_start': stitched_df.index.min(),
            'data_end': stitched_df.index.max()
        })
        
        pair_info['strict_qualified'] = True
        pair_info['strict_baseline'] = f"{baseline_period_used} ({baseline_years}yr)"
        print(f"✅ STRICT: Using {baseline_period_used} baseline ({baseline_years} years)")
    else:
        dropped_pairs.append(f"{pair_info['name']} - Only {baseline_years} baseline years")
        print(f"❌ STRICT: Only {baseline_years} years in baseline period")
    
    # Try inclusive approach
    if not baseline_period.empty and baseline_years >= MIN_BASELINE_YEARS:
        # Use standard baseline
        inclusive_baseline_avg = pair_baseline_avg
        inclusive_baseline_period = baseline_period_used
    else:
        # Use alternative baseline
        inclusive_baseline_avg, inclusive_baseline_period = calculate_alternative_baseline(
            stitched_df, BASELINE_START, BASELINE_END
        )
    
    if inclusive_baseline_avg is not None:
        monthly_avg = stitched_df.resample("M")["TMAX"].mean()
        pair_anomalies = monthly_avg - inclusive_baseline_avg
        
        inclusive_pairs.append({
            'pair_name': pair_info['name'],
            'anomalies': pair_anomalies,
            'baseline_temp': inclusive_baseline_avg,
            'baseline_period': inclusive_baseline_period,
            'data_start': stitched_df.index.min(),
            'data_end': stitched_df.index.max()
        })
        
        pair_info['inclusive_qualified'] = True
        pair_info['inclusive_baseline'] = inclusive_baseline_period
        print(f"✅ INCLUSIVE: Using {inclusive_baseline_period} baseline")
    else:
        print(f"❌ INCLUSIVE: Cannot establish any baseline")
    
    all_pair_info.append(pair_info)

# Step 6: Create Ensembles for Both Approaches
# --------------------------------------------
def create_ensemble(pair_list, approach_name):
    if not pair_list:
        print(f"\nNo valid pairs for {approach_name} approach.")
        return None, None
    
    print(f"\nCreating {approach_name} ensemble from {len(pair_list)} station pairs...")
    
    # Find full date range
    all_start_dates = [pair_data['data_start'] for pair_data in pair_list]
    all_end_dates = [pair_data['data_end'] for pair_data in pair_list]
    earliest_start = min(all_start_dates)
    latest_end = max(all_end_dates)
    
    # Create ensemble
    full_date_range = pd.date_range(start=earliest_start, end=latest_end, freq='M')
    all_anomalies = pd.DataFrame(index=full_date_range)
    
    for i, pair_data in enumerate(pair_list):
        all_anomalies[f'pair_{i}'] = pair_data['anomalies']
    
    ensemble_monthly_anomaly = all_anomalies.mean(axis=1, skipna=True)
    ensemble_monthly_anomaly = ensemble_monthly_anomaly.dropna()
    ensemble_annual_anomaly = ensemble_monthly_anomaly.resample("Y").mean()
    
    return ensemble_monthly_anomaly, ensemble_annual_anomaly

inclusive_monthly, inclusive_annual = create_ensemble(inclusive_pairs, "INCLUSIVE")
strict_monthly, strict_annual = create_ensemble(strict_pairs, "STRICT")

# Step 7: Create Interactive Map
# ------------------------------
def create_station_map():
    # Center map on continental US
    m = folium.Map(location=[39.8283, -98.5795], zoom_start=4, 
                   tiles='OpenStreetMap')
    
    # Add title
    title_html = '''
                 <h3 align="center" style="font-size:20px"><b>US Temperature Station Pairs</b></h3>
                 <p align="center" style="font-size:14px">
                 🟢 Strict Baseline (1960-1980) | 🔵 Inclusive Baseline | 🔴 Insufficient Data
                 </p>
                 '''
    m.get_root().html.add_child(folium.Element(title_html))
    
    for pair_info in all_pair_info:
        # Determine marker color and icon
        if pair_info['strict_qualified']:
            color = 'green'
            icon = 'star'
            popup_text = f"""
            <b>{pair_info['name']}</b><br>
            State: {pair_info['state']}<br>
            Data: {pair_info['data_start']}-{pair_info['data_end']}<br>
            <b>✅ STRICT:</b> {pair_info['strict_baseline']}<br>
            <b>✅ INCLUSIVE:</b> {pair_info['inclusive_baseline']}
            """
        elif pair_info['inclusive_qualified']:
            color = 'blue'
            icon = 'info-sign'
            popup_text = f"""
            <b>{pair_info['name']}</b><br>
            State: {pair_info['state']}<br>
            Data: {pair_info['data_start']}-{pair_info['data_end']}<br>
            <b>❌ STRICT:</b> Insufficient baseline data<br>
            <b>✅ INCLUSIVE:</b> {pair_info['inclusive_baseline']}
            """
        else:
            color = 'red'
            icon = 'remove'
            popup_text = f"""
            <b>{pair_info['name']}</b><br>
            State: {pair_info['state']}<br>
            Data: {pair_info['data_start']}-{pair_info['data_end']}<br>
            <b>❌ STRICT:</b> Insufficient baseline data<br>
            <b>❌ INCLUSIVE:</b> Cannot establish baseline
            """
        
        folium.Marker(
            location=[pair_info['lat'], pair_info['lon']],
            popup=folium.Popup(popup_text, max_width=300),
            tooltip=pair_info['name'].replace('_', ' ').title(),
            icon=folium.Icon(color=color, icon=icon)
        ).add_to(m)
    
    # Add legend
    legend_html = '''
    <div style="position: fixed; 
                bottom: 50px; left: 50px; width: 200px; height: 90px; 
                background-color: white; border:2px solid grey; z-index:9999; 
                font-size:14px; padding: 10px">
    <p><b>Station Qualification</b></p>
    <p><i class="fa fa-star" style="color:green"></i> Strict (1960-1980)</p>
    <p><i class="fa fa-info" style="color:blue"></i> Inclusive (Alt. baseline)</p>
    <p><i class="fa fa-remove" style="color:red"></i> Insufficient data</p>
    </div>
    '''
    m.get_root().html.add_child(folium.Element(legend_html))
    
    return m

# Create and save map
station_map = create_station_map()
station_map.save("station_pairs_map.html")
print(f"\n📍 Interactive map saved as 'station_pairs_map.html'")

# Step 8: Create Triple Comparison Plot (Annual + Monthly with LOESS)
# ------------------------------------------------------------------
if inclusive_annual is not None or strict_annual is not None:
    fig, axes = plt.subplots(3, 1, figsize=(14, 16))
    
    # Plot 1: Inclusive Approach (Annual)
    if inclusive_annual is not None:
        ax1 = axes[0]
        colors = ["#d62728" if x > 0 else "#1f77b4" for x in inclusive_annual]
        
        ax1.bar(inclusive_annual.index.year, inclusive_annual, 
                color=colors, alpha=0.8, width=0.8)
        
        rolling_avg = inclusive_annual.rolling(window=10, center=True, min_periods=5).mean()
        ax1.plot(rolling_avg.index.year, rolling_avg, color="black", linewidth=3, 
                label="10-Year Average", zorder=10)
        
        ax1.axhline(0, color="black", linestyle="--", alpha=0.5, linewidth=1)
        ax1.set_title(f"INCLUSIVE Approach: {len(inclusive_pairs)} Station Pairs (Annual)\n"
                     f"Mixed baselines: 1960-1980 + alternatives", 
                     fontsize=14, fontweight='bold', pad=15)
        ax1.set_ylabel("Temperature Anomaly (°C)", fontsize=12, fontweight='bold')
        ax1.legend(loc='upper left', fontsize=10)
        ax1.grid(axis="y", linestyle="--", alpha=0.3)
        ax1.tick_params(axis='both', which='major', labelsize=10)
        
        # Add stats
        recent_trend = inclusive_annual.tail(10).mean()
        stats_text = f"Recent 10yr: {recent_trend:+.2f}°C"
        ax1.text(0.02, 0.95, stats_text, transform=ax1.transAxes, 
                verticalalignment='top', fontsize=10, 
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
    else:
        axes[0].text(0.5, 0.5, 'No data available for Inclusive approach', 
                    ha='center', va='center', transform=axes[0].transAxes, fontsize=16)
        axes[0].set_title("INCLUSIVE Approach: No Data Available", fontsize=14, fontweight='bold')
    
    # Plot 2: Strict Approach (Annual)
    if strict_annual is not None:
        ax2 = axes[1]
        colors = ["#d62728" if x > 0 else "#1f77b4" for x in strict_annual]
        
        ax2.bar(strict_annual.index.year, strict_annual, 
                color=colors, alpha=0.8, width=0.8)
        
        rolling_avg = strict_annual.rolling(window=10, center=True, min_periods=5).mean()
        ax2.plot(rolling_avg.index.year, rolling_avg, color="black", linewidth=3, 
                label="10-Year Average", zorder=10)
        
        ax2.axhline(0, color="black", linestyle="--", alpha=0.5, linewidth=1)
        ax2.set_title(f"STRICT Approach: {len(strict_pairs)} Station Pairs (Annual)\n"
                     f"Uniform 1960-1980 baseline only", 
                     fontsize=14, fontweight='bold', pad=15)
        ax2.set_ylabel("Temperature Anomaly (°C)", fontsize=12, fontweight='bold')
        ax2.legend(loc='upper left', fontsize=10)
        ax2.grid(axis="y", linestyle="--", alpha=0.3)
        ax2.tick_params(axis='both', which='major', labelsize=10)
        
        # Add stats
        recent_trend = strict_annual.tail(10).mean()
        stats_text = f"Recent 10yr: {recent_trend:+.2f}°C"
        ax2.text(0.02, 0.95, stats_text, transform=ax2.transAxes, 
                verticalalignment='top', fontsize=10, 
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))
    else:
        axes[1].text(0.5, 0.5, 'No data available for Strict approach', 
                    ha='center', va='center', transform=axes[1].transAxes, fontsize=16)
        axes[1].set_title("STRICT Approach: No Data Available", fontsize=14, fontweight='bold')
    
    # Plot 3: Monthly Data with LOESS Smoothing
    if strict_monthly is not None:
        ax3 = axes[2]
        
        # Convert monthly index to numeric for LOESS
        monthly_data = strict_monthly.dropna()
        x_numeric = np.arange(len(monthly_data))
        
        # Plot monthly anomalies as light scatter
        ax3.scatter(monthly_data.index.year + monthly_data.index.month/12, 
                   monthly_data.values, alpha=0.3, s=8, color='gray', label='Monthly Anomalies')
        
        # Apply LOESS smoothing
        # Use a fraction that gives similar smoothing to 10-year rolling average
        loess_frac = min(0.1, max(0.02, 120/len(monthly_data)))  # Adaptive fraction
        
        try:
            loess_result = lowess(monthly_data.values, x_numeric, 
                                frac=loess_frac, it=3, return_sorted=True)
            
            # Convert x back to dates for plotting
            loess_dates = [monthly_data.index[int(x)] for x in loess_result[:, 0]]
            loess_years = [d.year + d.month/12 for d in loess_dates]
            
            ax3.plot(loess_years, loess_result[:, 1], 
                    color='red', linewidth=3, label='LOESS Smooth', zorder=10)
            
        except Exception as e:
            print(f"LOESS smoothing failed: {e}")
            # Fallback to rolling average
            rolling_monthly = monthly_data.rolling(window=120, center=True, min_periods=60).mean()
            ax3.plot(rolling_monthly.index.year + rolling_monthly.index.month/12, 
                    rolling_monthly.values, color='red', linewidth=3, 
                    label='10-Year Rolling Average', zorder=10)
        
        ax3.axhline(0, color="black", linestyle="--", alpha=0.5, linewidth=1)
        ax3.set_title(f"STRICT Approach: Monthly Anomalies with LOESS Smoothing\n"
                     f"{len(strict_pairs)} Station Pairs, Uniform 1960-1980 baseline", 
                     fontsize=14, fontweight='bold', pad=15)
        ax3.set_xlabel("Year", fontsize=12, fontweight='bold')
        ax3.set_ylabel("Temperature Anomaly (°C)", fontsize=12, fontweight='bold')
        ax3.legend(loc='upper left', fontsize=10)
        ax3.grid(axis="y", linestyle="--", alpha=0.3)
        ax3.tick_params(axis='both', which='major', labelsize=10)
        
        # Add stats for monthly data
        recent_monthly = monthly_data.tail(120).mean()  # Last 10 years of monthly data
        stats_text = f"Recent 10yr monthly avg: {recent_monthly:+.2f}°C\nLOESS fraction: {loess_frac:.3f}"
        ax3.text(0.02, 0.95, stats_text, transform=ax3.transAxes, 
                verticalalignment='top', fontsize=10, 
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
        
    else:
        axes[2].text(0.5, 0.5, 'No monthly data available for LOESS smoothing', 
                    ha='center', va='center', transform=axes[2].transAxes, fontsize=16)
        axes[2].set_title("Monthly LOESS Smoothing: No Data Available", fontsize=14, fontweight='bold')
    
    # Overall title and layout
    fig.suptitle("US Temperature Anomaly Ensemble Analysis\nInclusive vs. Strict Approaches + Monthly LOESS", 
                fontsize=16, fontweight='bold', y=0.98)
    
    # Add comprehensive footnote
    qualified_strict = [info for info in all_pair_info if info['strict_qualified']]
    qualified_inclusive = [info for info in all_pair_info if info['inclusive_qualified']]
    
    footnote_text = f"""
Strict Approach ({len(qualified_strict)} pairs): {', '.join([info['state'] for info in qualified_strict])}
Inclusive Approach ({len(qualified_inclusive)} pairs): {', '.join([info['state'] for info in qualified_inclusive])}
LOESS: Locally Weighted Scatterplot Smoothing - adaptive bandwidth for optimal trend detection
Data: NOAA GHCN-Daily & USCRN | Map: station_pairs_map.html
    """
    
    plt.figtext(0.02, 0.02, footnote_text.strip(), fontsize=9, 
                verticalalignment='bottom', wrap=True,
                bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgray', alpha=0.8))
    
    plt.subplots_adjust(bottom=0.15, top=0.92, hspace=0.4)
    plt.tight_layout()
    plt.show()
    
    # Print comprehensive summary
    print(f"\n{'='*80}")
    print(f"COMPREHENSIVE ENSEMBLE ANALYSIS WITH MONTHLY LOESS")
    print(f"{'='*80}")
    print(f"📊 INCLUSIVE Approach: {len(inclusive_pairs)} pairs (mixed baselines)")
    print(f"📊 STRICT Approach: {len(strict_pairs)} pairs (uniform 1960-1980 baseline)")
    print(f"📈 LOESS Smoothing: Applied to monthly data for trend detection")
    print(f"❌ Dropped pairs: {len(dropped_pairs)}")
    print(f"🗺️  Interactive map: station_pairs_map.html")
    
    if inclusive_annual is not None:
        print(f"\nINCLUSIVE Results (Annual):")
        print(f"  Years: {inclusive_annual.index.min().year}-{inclusive_annual.index.max().year}")
        print(f"  Recent 10yr avg: {inclusive_annual.tail(10).mean():+.2f}°C")
    
    if strict_annual is not None:
        print(f"\nSTRICT Results (Annual):")
        print(f"  Years: {strict_annual.index.min().year}-{strict_annual.index.max().year}")
        print(f"  Recent 10yr avg: {strict_annual.tail(10).mean():+.2f}°C")
    
    if strict_monthly is not None:
        print(f"\nSTRICT Results (Monthly with LOESS):")
        print(f"  Monthly data points: {len(strict_monthly)}")
        print(f"  LOESS fraction used: {loess_frac:.3f}")
        print(f"  Recent 10yr monthly avg: {strict_monthly.tail(120).mean():+.2f}°C")
    
    print(f"\nStation Qualification Summary:")
    for info in all_pair_info:
        status = "🟢 STRICT" if info['strict_qualified'] else ("🔵 INCLUSIVE" if info['inclusive_qualified'] else "🔴 INSUFFICIENT")
        print(f"  {status}: {info['name']} ({info['state']})")

else:
    print("No data available for either approach.")
