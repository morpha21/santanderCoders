CREATE TABLE acompanhante (
	nome VARCHAR(50),
	cpf VARCHAR(11) PRIMARY KEY NOT NULL,
	cpf_usuario VARCHAR(11) NOT NULL,
	CONSTRAINT FK_cpf_usuario FOREIGN KEY(cpf_usuario) REFERENCES hospede(cpf)
);
