% 13/09/2019 - Cadeias de markov 

clc; clear all; close all;

%% Aloha puro

N = 10;
a = 0.2;

uk = zeros(1,2);

for k = 1:length(uk)
    uk(k) = nchoosek(N,k-1) * (a^(k-1)) * ((1-a)^(N-(k-1)));
end

P_puro = [uk(1) 1-uk(1)-uk(2) uk(2); 
          uk(1) 1-uk(1) 0; 
          uk(1) 1-uk(1) 0];

Vazao_puro = N*a*((1-a)^(2*N-1));
Rb = 10e6;
T = 1/Rb;
Vazao_s_puro = Vazao_puro/T;
Vmax_puro = ((1-(1/(2*N)))^(2*N-1))/2;

a = 0:0.001:1;
Vazao_puro_vetor = N.*a.*((1-a).^(2*N-1));
figure(1)
plot(N.*a, Vazao_puro_vetor); hold on


%% Sloted


N = 10;
a = 0.2;

uk = zeros(1,2);

for k = 1:length(uk)
    uk(k) = nchoosek(N,k-1) * (a^(k-1)) * ((1-a)^(N-(k-1)));
end

P_slotted = [uk(1) 1-uk(1)-uk(2) uk(2); 
             uk(1) 1-uk(1)-uk(2) uk(2); 
             uk(1) 1-uk(1)-uk(2) uk(2)];

Vazao_slotted = N*a*(1-a)^(N-1);
aaaa = uk(1)*uk(2) + uk(2)*uk(2) + uk(2) * (1-uk(1)-uk(2));
Rb = 10e6;
T = 1/Rb;
Vazao_s_slotted = Vazao_slotted/T;
Vmax_slotted = (1-(1/N))^(N-1);  % a0 = 1/N

a = 0:0.001:1;
Vazao_slotted_vetor = N.*a.*(1-a).^(N-1);


figure(1)
plot(N.*a, Vazao_slotted_vetor);
title('Vazao - Aloha - N = 10');
xlabel('Na', 'FontWeight', 'bold');
ylabel('Vazao/epoca', 'FontWeight', 'bold');
legend('Puro', 'Slotted');
