% |Take 100 equal-spaced points in the interval|


format long

x = linspace(0,2*pi,100);
f = sin(x);
T = -x.^3/6 + x;

plot(x,f,'Color','k', 'LineWidth',1)
hold on
plot(x,T,'o','MarkerEdgeColor','b','MarkerSize',8,'LineWidth',1.5)
hold off

xlim([0,2*pi])
ylim([-3,1.25])
set(gca,'XTick',0:pi/2:2*pi)
set(gca,'XTickLabel',{'0','pi/2','pi','3*pi/2','2*pi'}) 
%% 
% 
% 
%