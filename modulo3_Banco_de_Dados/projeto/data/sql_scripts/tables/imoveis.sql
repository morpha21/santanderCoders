CREATE TABLE imoveis (
    id_imovel INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    cpf_proprietario VARCHAR(11),
    CONSTRAINT fk_cpf_proprietario FOREIGN KEY (cpf_proprietario) REFERENCES anfitriao(cpf),
    avaliacao FLOAT,
    preco_per_noite FLOAT,
    titulo VARCHAR(100),
    endereco VARCHAR(200),
    tipo_imovel VARCHAR(100),
    tipo_reserva VARCHAR(100),
    limite_hospede INT,
    descricao VARCHAR(2000),
    horario_checkin TIME,
    horario_checkout TIME
);
