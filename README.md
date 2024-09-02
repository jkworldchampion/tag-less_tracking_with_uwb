# tag-less_tracking_with_uwb

I suggest that passive position tracking system with two UWB device.  
Recently, the basic method of passive location tracking has three to four UWB equipment, has the singularity of the CIR created in the process of communication, and makes estimation.  
![image](https://github.com/user-attachments/assets/25c57206-22f5-4ec0-a21f-aaeffa2aa984)  
(Multistatic UWB Radar-Based Passive Human Tracking Using COTS Devices)  
  
The name of the method used at this time is called background subtraction. Accroding to "Passive Unsupervised Localization and Tracking using a Multi-Static UWB Radar Network" Kth background estimate: bk is calculate from b(k-1), 
Let mk, be a newly measured CIR at the kth. bk = a*b(k-1) + (1-a)*mk.  
  
And, using the Cell Averaging-Constant False Alarm Rate detector from the data (CIR) obtained from the above, we distinguish between noise and reflection signals.  
-> ![image](https://github.com/user-attachments/assets/f2576f47-dd32-4ad3-a93e-8c63bcdd2ac8)   
This formula organizes the target's coordinates (x, y), linearizes them using the Taylor series method, and leaves a part below the second order to complete the coordinate estimation through the LS approach.  

