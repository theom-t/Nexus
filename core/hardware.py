import subprocess
import os

def detect_gpu():
    """
    Attempts to identify the local GPU using nvidia-smi.
    Returns a string identifier (e.g., 'RTX 5090', 'Jetson Orin', 'Generic GPU').
    """
    try:
        # Check for nvidia-smi (Standard GPUs)
        res = subprocess.check_output(["nvidia-smi", "--query-gpu=name", "--format=csv,noheader"]).decode("utf-8")
        gpu_name = res.strip().split("\n")[0]
        return gpu_name
    except:
        # Check for Jetson (tegrastats usually available)
        if os.path.exists("/usr/bin/tegrastats"):
            return "Jetson Orin Nano"
        return "Generic/CPU"

def get_hardware_constraints(gpu_name: str) -> str:
    """
    Returns relevant engineering constraints for the detected hardware.
    """
    if "5090" in gpu_name or "Blackwell" in gpu_name:
        return "HARDWARE: Blackwell (RTX 5090) detected. Prioritize CUDA 13.0, CuPy, and TF-Nightly optimizations."
    elif "Orin" in gpu_name:
        return "HARDWARE: Jetson Orin Nano detected. Prioritize NVDLA, power-efficient inference, and TensorRT."
    elif "Apple" in gpu_name or "MPS" in gpu_name:
        return "HARDWARE: Apple Silicon detected. Prioritize MPS (Metal Performance Shaders) and MLX."
    return "HARDWARE: Generic/CPU environment. Focus on standard Python/C++ optimizations."
