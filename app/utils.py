import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from typing import List, Dict, Tuple

def load_data(country: str) -> pd.DataFrame:
    """Load and prepare data for a specific country."""
    df = pd.read_csv(f'data/{country.lower()}_clean.csv')
    df['Country'] = country
    return df

def get_summary_stats(df: pd.DataFrame, metrics: List[str]) -> pd.DataFrame:
    """Calculate summary statistics for specified metrics."""
    return df[metrics].agg(['mean', 'median', 'std']).round(2)

def create_boxplot(df: pd.DataFrame, metric: str) -> go.Figure:
    """Create an interactive boxplot using plotly."""
    fig = px.box(df, x='Country', y=metric,
                 title=f'{metric} Distribution by Country',
                 labels={'y': f'{metric} (W/m²)'})
    fig.update_layout(
        template='plotly_white',
        showlegend=False,
        height=500
    )
    return fig

def create_time_series(df: pd.DataFrame, metric: str) -> go.Figure:
    """Create an interactive time series plot."""
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    fig = px.line(df, x='Timestamp', y=metric,
                  title=f'{metric} Over Time',
                  labels={'y': f'{metric} (W/m²)'})
    fig.update_layout(
        template='plotly_white',
        height=500
    )
    return fig

def get_top_regions(df: pd.DataFrame, metric: str, n: int = 5) -> pd.DataFrame:
    """Get top N regions based on a specific metric."""
    return df.nlargest(n, metric)[['Country', metric]].round(2)

def calculate_correlation(df: pd.DataFrame, metrics: List[str]) -> pd.DataFrame:
    """Calculate correlation matrix for specified metrics."""
    return df[metrics].corr().round(2)

def get_metric_description(metric: str) -> str:
    """Get description for a specific metric."""
    descriptions = {
        'GHI': 'Global Horizontal Irradiance - Total solar radiation received on a horizontal surface',
        'DNI': 'Direct Normal Irradiance - Direct solar radiation received on a surface perpendicular to the sun',
        'DHI': 'Diffuse Horizontal Irradiance - Scattered solar radiation received on a horizontal surface'
    }
    return descriptions.get(metric, 'No description available')
