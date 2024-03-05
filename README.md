# gFHR (General Fluoride-Salt-Cooled High-Temperature Reactor) Data

This data set is for the gFHR (General Fluoride-Salt-Cooled High-Temperature Reactor) Load Follows (LF) case. The power is brought from 100% down to 50% and back up to 100% in 10% intervals every hour.


### Version
Last Updated: March 5, 2024

### Data 
Below is the description of each dataset:

|Filename|Description|Size|SAM Run Time [s]|
|----|-----|-----|-----|
|```gFHR-LF-1.csv```|Load Follows. 100% power -> 50% power -> 100% power, 10 power changes, 1 hour intervals| (1803,151)|~|
|```gFHR-LF-2.csv```|Random power changes. 10% increments, hold for 1 hour, 72 power changes|(12189, 151)|~|
|```gFHR-LF-3.csv```|Random power changes. 5% increments, hold for 1 hour, 10 power changes|(1868, 151)|~|
|```gFHR-LF-4.csv```|Random power changes. 5% increments, hold for 10 minutes, 300 power changes|(15926, 151)|112241.01|
|```gFHR-LF-5.csv```|Random power changes. 5% increments, hold for 10 minutes, 250 power changes|(16230, 151)|105545.55|
|```gFHR-LF-6.csv```|Random power changes. 5% increments, hold for 15-20 minutes, 200 power changes|(14133, 151)|91346.42|

The input and states are listed in the tables below:

**Input**  
|Variable|Description|Units|
|----|-----|-----|
|```target_power```|$\dot{Q}_{RX,T}$ : Target reactor power|W|

**States**  
|Variable|Description|Units|
|----|-----|-----|
|```core_in_T```|$T_{c,in}$ : Core Inlet Temperature|K|
|```core_out_T```|$T_{c,out}$ : Core Inlet Temperature|K|
|```core_in_P```|$P_{c,in}$ : Core Inlet Pressure|Pa|
|```core_out_P```|$P_{c,out}$ : Core Outlet Pressure|Pa|
|```IHX_primary_in_T```|$T_{ihx,p,in}$ : IHX Primary Inlet Temperature|K|
|```IHX_primary_out_t```|$T_{ihx,p,out}$ : IHX Primary Outlet Temperature|K|
|```IHX_primary_in_P```|$P_{ihx,p,in}$ : IHX Primary Inlet Pressure|Pa|
|```IHX_primary_out_P```|$P_{ihx,p,out}$ : IHX Primary Outlet Pressure|Pa|
|```IHX_secondary_in_T```|$T_{ihx,s,out}$ : IHX Secondary Inlet Temperature|K|
|```IHX_secondary_out_t```|$T_{ihx,s,out}$ : IHX Secondary Outlet Temperature|K|
|```IHX_secondary_in_P```|$P_{ihx,s,in}$ : IHX Secondary Inlet Pressure|Pa|
|```IHX_secondary_out_P```|$P_{ihx,s,out}$ : IHX Secondary Outlet Pressure|Pa|
|```Core_flow```|$\dot{m}_p$ : Primary Mass Flow Rate|kg/s|
|```secondary_flow```|$\dot{m}_s$ : Secondary Mass Flow Rate|kg/s|
|```IHX_energy```|$\dot{Q}_{HX}$ : IHX Head Extraction Rate|*|
|```SG_energy```|$\dot{Q}_{SG}$ : SG Head Extraction Rate|*|
|```core_energy```|$\dot{Q}_{RX}$ : Reactor Core Power|W|
|```C1```|$C_1$ : Group-1 Delayed Neutron Precursor Concentration|*|
|```C2```|$C_2$ : Group-2 Delayed Neutron Precursor Concentration|*|
|```C3```|$C_3$ : Group-3 Delayed Neutron Precursor Concentration|*|
|```C4```|$C_4$ : Group-4 Delayed Neutron Precursor Concentration|*|
|```C5```|$C_5$ : Group-5 Delayed Neutron Precursor Concentration|*|
|```C6```|$C_6$ : Group-6 Delayed Neutron Precursor Concentration|*|
|```moderator_Reactivity```|$\rho_m$ : Moderator Reactivity Feedback|*|
|```coolant_Reactivity```|$\rho_c$ : Coolant reactivity feedback|*|
|```CRD_pos:value```|$z_{cr}$ : Control Rod Position |m|
|```Pump:pump_head```|$\Delta P _p$ : Primary Pump Head|Pa|
|```Solar-pump:pump_head```|$\Delta P_s$ : Secondary PUmp Head|Pa|
_* TO ADD units_

**Supplementary States**  
These state values can be used to assist in predictions. They are not on the states requirements list, but I [Jasmin Lim] have used them to predict other state values.
|Variable|Description|Units|
|----|-----|-----|
|```Pump:pump_RPM```|$n_p$ : Primary Pump Speed|RPM|
|```Solar-pump:pump_RPM```|$n_s$ : Secondary Pump Speed|RPM|
|```C_I135```|$N_{I}$ : Iodine-135 Global Concentration|$\Delta$k/k|
|```C_XE135```|$N_{Xe}$ : Xenon-135 Global Concentration|$\Delta$k/k|

### Accessing the data

Use the following list of column names to import the data:
```
col_names = ["time",
             "target_power",
             "core_in_T",
             "core_out_T",
             "core_in_P",
             "core_out_P",
             "IHX_primary_in_T",
             "IHX_primary_out_t",
             "IHX_primary_in_P",
             "IHX_primary_out_P",
             "IHX_secondary_in_T",
             "IHX_secondary_out_t",
             "IHX_secondary_in_P",
             "IHX_secondary_out_P",
             "Core_flow",
             "secondary_flow",
             "IHX_energy",
             "SG_energy",
             "core_energy",
             "C1",
             "C2",
             "C3",
             "C4",
             "C5",
             "C6",
             "moderator_Reactivity",
             "coolant_Reactivity",
             "CRD_pos:value",
             "Pump:pump_head",
             "Solar-pump:pump_head"]

col_names_supp = ["Pump:pump_RPM",
                  "Solar-pump:pump_RPM",
                  "C_I135",
                  "C_I135"]
```

