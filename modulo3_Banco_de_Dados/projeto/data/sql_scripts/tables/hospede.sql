CREATE TABLE hospede (
    cpf VARCHAR(11) PRIMARY KEY NOT NULL,
    nome VARCHAR(100),
    email VARCHAR(60),
    telefone VARCHAR(20),
    meio_pagamento VARCHAR(16),
    avaliacao FLOAT
);
