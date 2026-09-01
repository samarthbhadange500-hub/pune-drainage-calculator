import math

def calculate_peak_runoff(c, i_mm_hr, a_hectares):
    """
    Calculates Peak Surface Runoff using the Rational Method (Q = CiA / 360).
    
    Parameters:
    c (float): Runoff coefficient (e.g., 0.85 for concrete/asphalt streets).
    i_mm_hr (float): Rainfall intensity in mm/hr for the design storm in Pune.
    a_hectares (float): Catchment area in hectares.
    
    Returns:
    float: Peak discharge (Q) in cubic meters per second (m^3/s).
    """
    # Conversion factor 360 handles units: (mm/hr) and (hectares) to (m^3/s)
    q_peak = (c * i_mm_hr * a_hectares) / 360
    return q_peak

def calculate_pipe_diameter(q_req, n, s):
    """
    Calculates the required circular pipe diameter using Manning's Equation
    assuming the pipe is flowing full to handle the peak discharge.
    
    Parameters:
    q_req (float): Required discharge capacity (m^3/s).
    n (float): Manning's roughness coefficient (e.g., 0.013 for concrete pipes).
    s (float): Slope of the energy grade line or pipe bed (m/m).
    
    Returns:
    float: Required internal pipe diameter in meters.
    """
    # Manning's equation for a full circular pipe:
    # Q = (1/n) * A * R^(2/3) * S^(1/2)
    # Where Area A = (pi * D^2) / 4
    # Hydraulic Radius R = D / 4
    # Solving for D: D = [ (Q * n * 4^(5/3)) / (pi * S^(1/2)) ] ^ (3/8)
    
    term1 = q_req * n * (4 ** (5/3))
    term2 = math.pi * math.sqrt(s)
    
    diameter = (term1 / term2) ** (3/8)
    return diameter

# --- Example Execution for Pune Drainage Sector ---

if __name__ == "__main__":
    # 1. Catchment & Rainfall Parameters
    catchment_area = 5.0       # Hectares
    rainfall_intensity = 75.0  # mm/hr (Design storm intensity for Pune)
    runoff_coefficient = 0.80  # Highly developed urban street area
    
    # Calculate Runoff
    peak_discharge = calculate_peak_runoff(runoff_coefficient, rainfall_intensity, catchment_area)
    
    # 2. Drainage Pipe Parameters
    manning_n = 0.013          # Standard for RCC (Reinforced Cement Concrete) pipes
    pipe_slope = 0.002         # 0.2% bed slope
    
    # Calculate Required Pipe Size
    req_diameter = calculate_pipe_diameter(peak_discharge, manning_n, pipe_slope)
    
    print("-" * 50)
    print("HYDROLOGIC & HYDRAULIC RUNOFF ESTIMATION")
    print("-" * 50)
    print(f"Catchment Area       : {catchment_area} hectares")
    print(f"Rainfall Intensity   : {rainfall_intensity} mm/hr")
    print(f"Estimated Peak Runoff: {peak_discharge:.3f} cubic meters / second")
    print("-" * 50)
    print(f"Pipe Bed Slope       : {pipe_slope} m/m")
    print(f"Required RCC Pipe Dia: {req_diameter:.3f} meters ({req_diameter * 1000:.0f} mm)")
    
    # Standardize to nearest commercial pipe size (e.g., multiples of 150mm/300mm)
    commercial_dia = math.ceil((req_diameter * 1000) / 150.0) * 150
    print(f"Recommended standard commercial pipe size: {commercial_dia} mm")
    print("-" * 50)
    