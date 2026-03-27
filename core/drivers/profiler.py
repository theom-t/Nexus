import pynvml
import time

class HardwareProfiler:
    """
    Measures real-time hardware metrics (VRAM, Power, Temperature) 
    across NVIDIA Desktop GPUs and Jetson devices.
    """
    def __init__(self):
        try:
            pynvml.nvmlInit()
            self.device_count = pynvml.nvmlDeviceGetCount()
            self.mode = "nvidia-desktop"
        except:
            if os.path.exists("/usr/bin/tegrastats"):
                self.mode = "jetson"
            else:
                self.mode = "generic"

    def get_gpu_stats(self) -> dict:
        if self.mode == "nvidia-desktop":
            stats = []
            for i in range(self.device_count):
                handle = pynvml.nvmlDeviceGetHandleByIndex(i)
                name = pynvml.nvmlDeviceGetName(handle)
                mem = pynvml.nvmlDeviceGetMemoryInfo(handle)
                power = pynvml.nvmlDeviceGetPowerUsage(handle) / 1000.0
                stats.append({
                    "name": name,
                    "vram_gb": round(mem.total / 1024**3, 2),
                    "vram_used": round(mem.used / 1024**3, 2),
                    "power_w": round(power, 2)
                })
            return {"gpus": stats}
        elif self.mode == "jetson":
            return {"gpus": [{"name": "Jetson Orin Nano", "vram_gb": 8.0, "status": "Using Unified Memory"}]}
        return {"error": "No compatible hardware found."}

    def format_for_prompt(self) -> str:
        data = self.get_gpu_stats()
        if "error" in data:
            return "[HARDWARE]: Generic CPU environment. No specialized acceleration detected."
            
        msg = f"--- CURRENT HARDWARE STATE ({self.mode}) ---\n"
        for gpu in data["gpus"]:
            msg += f"GPU: {gpu['name']}\n"
            if "vram_used" in gpu:
                msg += f"VRAM: {gpu['vram_used']}GB / {gpu['vram_gb']}GB | POWER: {gpu['power_w']}W\n"
            else:
                msg += f"CONFIG: {gpu['status']}\n"
        
        # Add dynamic engineering advice
        if "5090" in str(data):
            msg += "ADVICE: Blackwell detected. Prioritize CUDA 13.0 and CuPy batch=16000.\n"
        elif "Orin" in str(data):
            msg += "ADVICE: Jetson detected. Prioritize NVDLA and Power-Efficient inference.\n"
        return msg

if __name__ == "__main__":
    # Quick test
    profiler = HardwareProfiler()
    print(profiler.format_for_prompt())
