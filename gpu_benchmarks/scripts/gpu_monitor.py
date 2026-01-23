#!/usr/bin/env python3
"""
Real-time GPU monitoring dashboard
"""
import time
import pynvml
from datetime import datetime

class GPUMonitor:
    def __init__(self):
        pynvml.nvmlInit()
        self.device_count = pynvml.nvmlDeviceGetCount()

    def get_gpu_info(self, gpu_id=0):
        """Get current GPU stats"""
        handle = pynvml.nvmlDeviceGetHandleByIndex(gpu_id)

        info = {
            'name': pynvml.nvmlDeviceGetName(handle),
            'temperature': pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU),
            'power_usage': pynvml.nvmlDeviceGetPowerUsage(handle) / 1000.0,  # mW to W
            'power_limit': pynvml.nvmlDeviceGetPowerManagementLimit(handle) / 1000.0,
            'fan_speed': pynvml.nvmlDeviceGetFanSpeed(handle),
            'utilization': pynvml.nvmlDeviceGetUtilizationRates(handle),
            'memory': pynvml.nvmlDeviceGetMemoryInfo(handle),
            'clocks': {
                'graphics': pynvml.nvmlDeviceGetClockInfo(handle, pynvml.NVML_CLOCK_GRAPHICS),
                'sm': pynvml.nvmlDeviceGetClockInfo(handle, pynvml.NVML_CLOCK_SM),
                'memory': pynvml.nvmlDeviceGetClockInfo(handle, pynvml.NVML_CLOCK_MEM),
            }
        }
        return info

    def monitor_continuous(self, interval=1.0, duration=None):
        """Monitor GPU continuously"""
        print("GPU Monitoring Dashboard")
        print("=" * 80)
        print("Press Ctrl+C to stop\n")

        start_time = time.time()
        try:
            while True:
                if duration and (time.time() - start_time) > duration:
                    break

                for gpu_id in range(self.device_count):
                    info = self.get_gpu_info(gpu_id)

                    print(f"\n[GPU {gpu_id}] {info['name']} - {datetime.now().strftime('%H:%M:%S')}")
                    print(f"  Temperature:   {info['temperature']}°C")
                    print(f"  Power:         {info['power_usage']:.1f}W / {info['power_limit']:.1f}W ({info['power_usage']/info['power_limit']*100:.1f}%)")
                    print(f"  Fan Speed:     {info['fan_speed']}%")
                    print(f"  GPU Util:      {info['utilization'].gpu}%")
                    print(f"  Memory Util:   {info['utilization'].memory}%")
                    print(f"  Memory:        {info['memory'].used / 1024**2:.0f}MB / {info['memory'].total / 1024**2:.0f}MB ({info['memory'].used/info['memory'].total*100:.1f}%)")
                    print(f"  GPU Clock:     {info['clocks']['graphics']} MHz")
                    print(f"  Memory Clock:  {info['clocks']['memory']} MHz")

                time.sleep(interval)
                print("\n" + "=" * 80)

        except KeyboardInterrupt:
            print("\n\nMonitoring stopped.")
        finally:
            pynvml.nvmlShutdown()

    def __del__(self):
        try:
            pynvml.nvmlShutdown()
        except:
            pass

if __name__ == "__main__":
    import sys

    interval = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0
    duration = float(sys.argv[2]) if len(sys.argv) > 2 else None

    monitor = GPUMonitor()
    monitor.monitor_continuous(interval=interval, duration=duration)
