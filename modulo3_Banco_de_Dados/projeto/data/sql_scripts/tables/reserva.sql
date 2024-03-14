CREATE TABLE reserva (
	id_reserva INT NOT NULL AUTO_INCREMENT,
	PRIMARY KEY (id_reserva),
	qnt_hospede INT,
	cpf_hospede VARCHAR(11),
	CONSTRAINT fk_cpf_hospede FOREIGN KEY (cpf_hospede) REFERENCES hospede(cpf),
	id_imovel INT,
	CONSTRAINT fk_id_imovel FOREIGN KEY (id_imovel) REFERENCES imovel(id_imovel),
	check_in DATE,
	check_out DATE
);
