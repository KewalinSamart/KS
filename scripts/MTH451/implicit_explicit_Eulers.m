% Euler's Implicit vs Explicit Method
% y' = -20(y-t^2)+2t; y(0) = 1/3; 0 <= t <= 1
y0 = 1/3;
t0 = 0;
tmax = 1;
h = 0.1;
N = (tmax-t0)/h;

% initialize solutions
T = [0;h;tmax]';
Yex = zeros(N+1,1);
Yex(1) = y0;
Yim = zeros(N+1,1);
Yim(1) = y0;

% Solve using Euler's Implicit Method
for i = 1:N
    t = T(i)+h;
    y = fsolve(@(y) y-Yex(i)+h*(-20*(y-t^2)+2*t), Yex(i));
    
    T(i+1) = t;
    Yex(i+1) = y;
end

% Solve using Euler's Explicit Method
for i = 1:N
    fi = -20*(Yim(i)-T(i))+2*T(i);
    Yim(i+1) = Yim(i)+h*fi   ; 
end


% Plot
T_ = linspace(0,1,100);
sol_exact = T_.^2+1/3*exp(-20*T_);

figure; hold on

explicit_plot = plot(T,Yex,'-.','MarkerSize',20);
implicit_plot = plot(T,Yim,'-.','MarkerSize',20);
exact_plot = plot(T_,sol_exact,'-','LineWidth',2);

legend([explicit_plot;implicit_plot;exact_plot], 'Forward Eulers','Backward Eulers','Exact solution');
xlabel('t')
ylabel('solutions for y')
title('Forward and Backward Eulers Methods with h = 0.1')
hold off