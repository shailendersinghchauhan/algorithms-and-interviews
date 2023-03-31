class ControlModel:
    def __init__(self, setpoint, kp, ki, kd, output_limits=None, sample_time=1):
        self.setpoint = setpoint
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.sample_time = sample_time
        self.output_limits = output_limits
        self.integral = 0
        self.derivative = 0
        self.last_error = 0
        self.last_output = None
        self.last_time = None

    def update(self, measurement):
        error = self.setpoint - measurement
        current_time = time.time()
        dt = current_time - self.last_time if self.last_time is not None else self.sample_time

        self.integral += error * dt
        self.derivative = (error - self.last_error) / dt if self.last_time is not None else 0
        output = self.kp * error + self.ki * self.integral + self.kd * self.derivative

        if self.output_limits is not None:
            output = max(min(output, self.output_limits[1]), self.output_limits[0])

        self.last_error = error
        self.last_output = output
        self.last_time = current_time

        return output
