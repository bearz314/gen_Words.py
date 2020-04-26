%% Plot the figure

set(0,'DefaultAxesFontSize' ,15)

% Create new graph and set positions
hFig = figure;
set(hFig, 'Position', [0 0 1270 500]);

% Perform dummy calculations for temperature
t = (1:days(1):days(15))+datetime;
temp1 = rand(15,1)*20 + 10;
temp2 = rand(15,1)*20 + 10;

% Plot the temperature figure
ymax = max(temp1,temp2);
ymin = min(temp1,temp2);
% Nice formattings
plot(t,ymin,'o-', t,ymax,'o-')
xl=xlim; ax=gca; ax.XAxis.MinorTick='on'; ax.XAxis.MinorTickValues=xl(1):days(1):xl(2);
grid minor
legend('Min T', 'Max T')
ylabel('Temperature /C')

%% Save the figure
saveas(hFig, 'image1', 'emf');
close all;

% Export data
txt = fopen('out.txt', 'w');
fprintf(txt,'%s\n',datestr(t(end),'DD-mm-YY'));   % last date
for i=1:7
    fprintf(txt,'%s\n',datestr(t(i),'DD-mm-YY')); % dates
end
for i=1:7
    fprintf(txt,'%d%%\n',round(rand()*50+50));    % percentage
end
% description
fprintf(txt,'Partly cloudy. Slight chance of a shower, most likely in the morning. Light winds becoming northeasterly 15 to 20 km/h during the afternoon then becoming light during the evening.');

fclose(txt);






