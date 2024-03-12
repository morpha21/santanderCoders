CREATE TABLE reserva (
	id_reserva INT NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (id_reserva),
	cpf_hospede VARCHAR(11),
	CONSTRAINT fk_cpf_hospede FOREIGN KEY (cpf_hospede) REFERENCES hospede(cpf),
	id_imovel INT,
	CONSTRAINT fk_id_imovel FOREIGN KEY (id_imovel) REFERENCES imoveis(id_imovel),
	checkin DATE,
	checkout DATE,
	acompanhantes INT
);
