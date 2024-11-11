export interface Aula {
  id: number;
  titulo: string;
  descricao: string;
  data_hora: string;
  instrutor: {
      id: number;
      username: string;
    };
  total_participantes: number;
}
