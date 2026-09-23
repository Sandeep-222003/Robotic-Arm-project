<?xml version="1.0" ?>
<robot name="cyberpunk_4wd_base">

  <!-- ================= MATERIALS ================= -->
  <material name="matte_black">  <color rgba="0.12 0.12 0.14 1.0"/> </material>
  <material name="neon_cyan">    <color rgba="0.0 1.0 0.8 1.0"/>  </material>
  <material name="power_red">    <color rgba="0.8 0.1 0.1 1.0"/>  </material>
  <material name="pcb_green">    <color rgba="0.1 0.4 0.2 1.0"/>  </material>
  <material name="heatsink_silver"><color rgba="0.7 0.7 0.75 1.0"/> </material>
  <material name="rubber_dark">  <color rgba="0.05 0.05 0.05 1.0"/> </material>

  <!-- ================= UNIBODY CHASSIS ================= -->
  <link name="base_chassis">
    <visual>
      <!-- Wider and longer single plate: 280mm x 200mm x 6mm -->
      <geometry> <box size="0.28 0.20 0.006"/> </geometry>
      <material name="matte_black"/>
    </visual>
  </link>

  <!-- ================= 4-WHEEL DRIVE SYSTEM ================= -->
  <!-- Front Left -->
  <joint name="fl_wheel_joint" type="continuous">
    <parent link="base_chassis"/>
    <child link="fl_wheel"/>
    <origin xyz="0.09 0.115 -0.015" rpy="1.5708 0 0"/>
    <axis xyz="0 0 1"/>
  </joint>
  <link name="fl_wheel">
    <visual>
      <geometry> <cylinder radius="0.0325" length="0.026"/> </geometry>
      <material name="rubber_dark"/>
    </visual>
  </link>

  <!-- Rear Left -->
  <joint name="rl_wheel_joint" type="continuous">
    <parent link="base_chassis"/>
    <child link="rl_wheel"/>
    <origin xyz="-0.09 0.115 -0.015" rpy="1.5708 0 0"/>
    <axis xyz="0 0 1"/>
  </joint>
  <link name="rl_wheel">
    <visual>
      <geometry> <cylinder radius="0.0325" length="0.026"/> </geometry>
      <material name="rubber_dark"/>
    </visual>
  </link>

  <!-- Front Right -->
  <joint name="fr_wheel_joint" type="continuous">
    <parent link="base_chassis"/>
    <child link="fr_wheel"/>
    <origin xyz="0.09 -0.115 -0.015" rpy="1.5708 0 0"/>
    <axis xyz="0 0 1"/>
  </joint>
  <link name="fr_wheel">
    <visual>
      <geometry> <cylinder radius="0.0325" length="0.026"/> </geometry>
      <material name="rubber_dark"/>
    </visual>
  </link>

  <!-- Rear Right -->
  <joint name="rr_wheel_joint" type="continuous">
    <parent link="base_chassis"/>
    <child link="rr_wheel"/>
    <origin xyz="-0.09 -0.115 -0.015" rpy="1.5708 0 0"/>
    <axis xyz="0 0 1"/>
  </joint>
  <link name="rr_wheel">
    <visual>
      <geometry> <cylinder radius="0.0325" length="0.026"/> </geometry>
      <material name="rubber_dark"/>
    </visual>
  </link>

  <!-- ================= ROBOTIC ARM MOUNTING PAD ================= -->
  <!-- Placed front-center for maximum reach and stability -->
  <joint name="arm_mount_joint" type="fixed">
    <parent link="base_chassis"/>
    <child link="arm_mount_pad"/>
    <origin xyz="0.09 0 0.005" rpy="0 0 0"/> 
  </joint>
  <link name="arm_mount_pad">
    <visual>
      <!-- Circular reinforcement ring for the Ch0 Base Swivel -->
      <geometry> <cylinder radius="0.04" length="0.005"/> </geometry>
      <material name="neon_cyan"/>
    </visual>
  </link>

  <!-- ================= ELECTRONICS LAYOUT ================= -->
  <!-- Left Motor Driver (Controls Front/Rear Left Wheels) -->
  <joint name="driver1_joint" type="fixed">
    <parent link="base_chassis"/>
    <child link="motor_driver_left"/>
    <origin xyz="0 0.07 0.015" rpy="0 0 0"/>
  </joint>
  <link name="motor_driver_left">
    <visual>
      <geometry> <box size="0.045 0.045 0.02"/> </geometry>
      <material name="heatsink_silver"/>
    </visual>
  </link>

  <!-- Right Motor Driver (Controls Front/Rear Right Wheels) -->
  <joint name="driver2_joint" type="fixed">
    <parent link="base_chassis"/>
    <child link="motor_driver_right"/>
    <origin xyz="0 -0.07 0.015" rpy="0 0 0"/>
  </joint>
  <link name="motor_driver_right">
    <visual>
      <geometry> <box size="0.045 0.045 0.02"/> </geometry>
      <material name="heatsink_silver"/>
    </visual>
  </link>

  <!-- Battery & Buck Converter (Dead Center) -->
  <joint name="battery_joint" type="fixed">
    <parent link="base_chassis"/>
    <child link="battery_pack"/>
    <origin xyz="-0.02 0 0.015" rpy="0 0 0"/>
  </joint>
  <link name="battery_pack">
    <visual>
      <geometry> <box size="0.10 0.035 0.025"/> </geometry>
      <material name="power_red"/>
    </visual>
  </link>

  <!-- Raspberry Pi 5 (Rear Left) -->
  <joint name="rpi_joint" type="fixed">
    <parent link="base_chassis"/>
    <child link="raspberry_pi"/>
    <origin xyz="-0.10 0.06 0.01" rpy="0 0 0"/>
  </joint>
  <link name="raspberry_pi">
    <visual>
      <geometry> <box size="0.085 0.056 0.015"/> </geometry>
      <material name="pcb_green"/>
    </visual>
  </link>

  <!-- ESP32 & PCA9685 Cluster (Rear Right) -->
  <joint name="esp_pca_joint" type="fixed">
    <parent link="base_chassis"/>
    <child link="microcontroller_cluster"/>
    <origin xyz="-0.10 -0.06 0.01" rpy="0 0 0"/>
  </joint>
  <link name="microcontroller_cluster">
    <visual>
      <geometry> <box size="0.06 0.05 0.01"/> </geometry>
      <material name="matte_black"/>
    </visual>
  </link>

  <!-- ================= FRONT SENSORS ================= -->
  <!-- Ultrasonic & Camera Bracket -->
  <joint name="sensor_bracket_joint" type="fixed">
    <parent link="base_chassis"/>
    <child link="sensor_array"/>
    <origin xyz="0.14 0 0.01" rpy="0 0 0"/>
  </joint>
  <link name="sensor_array">
    <visual>
      <geometry> <box size="0.01 0.06 0.03"/> </geometry>
      <material name="neon_cyan"/>
    </visual>
  </link>

  <!-- ================= REAR UI (SWITCHES) ================= -->
  <joint name="ui_panel_joint" type="fixed">
    <parent link="base_chassis"/>
    <child link="rear_ui_panel"/>
    <origin xyz="-0.14 0 0.005" rpy="0 0 0"/>
  </joint>
  <link name="rear_ui_panel">
    <visual>
      <geometry> <box size="0.01 0.08 0.01"/> </geometry>
      <material name="power_red"/>
    </visual>
  </link>

</robot>
