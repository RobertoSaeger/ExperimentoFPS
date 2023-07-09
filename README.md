# ExperimentoFPS
Experimento para determinar o menor FPS de video gerado por um UAV, que ainda garanta consciencia situacional.
O experimento foi feito no simulador de voo Great Planes Real Flight Simulator rodando no programa SimulaFPS.cpp que roda o simulador por 
dois minutos e depois reduz o frame rate para 10, 8, 6, 4 e 2 FPS. O teste é interrompido quando o piloto perde a capacidade de 
controlar o voo ou quando o 2 FPS é atingido. 
Os resultados estão no arquivo Resumo2ExperimentoSimulador.csv
O arquivo ExperimentoFPS.csv traz os dados formatados para uso em colab.
No arquivo Experiment4FPS temos os valores 1 para Drone Recreativo, 2 para Radio controle, 3 para Drone Profissional e 4 para Gamer na coluna Specialty;
e os valores 1 para sim e 0 para não na coluna Training a coluna FPS registra o último FPS que permitiu controle ao piloto.
