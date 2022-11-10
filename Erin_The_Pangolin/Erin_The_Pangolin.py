# assumption: the list of peaks is ordered

peaks = [1335, 1439, 987, 312, 871, 1461, 1171, 654, 123]

# first solution: the pangolin only goes forward, one peak after the other

maxPeakIndex = 0,
#diff = 0

maxDiff = 0;

for i in range(len(peaks)-1):
    if peaks[i] - peaks[i+1] > maxDiff:
        maxPeakIndex=i
        maxDiff=peaks[i] - peaks[i+1]

print(maxDiff, maxPeakIndex, peaks[maxPeakIndex], peaks[maxPeakIndex + 1])

# second solution: after having reached the peak, the pangolin can roll back or forward

peaks = [1335, 1439, 312, 987, 871, 1461, 1171, 654, 123]

maxPeakIndex = 0,
toTheRight = True
#diff = 0

maxDiff = 0;

for i in range(len(peaks)-1):
    if abs(peaks[i] - peaks[i+1]) > maxDiff:
        if peaks[i] > peaks[i+1]:
            maxPeakIndex = i
            toTheRight = True
        else:
            maxPeakIndex = i + 1
            toTheRight = False
        maxDiff = abs(peaks[i] - peaks[i+1])

print(maxDiff, maxPeakIndex, peaks[maxPeakIndex], toTheRight)])
