#-----------------------------------------------aluga----------------------------------------
DELIMITER $
CREATE TRIGGER VerificaAlugaCarro BEFORE insert
ON aluga
FOR EACH ROW
BEGIN
	call VerificaProcAlugaCarro(NEW.id_carro_fk);
	
END$
DELIMITER ;

#-----------------------------------------------cliente----------------------------------------
DELIMITER $
CREATE TRIGGER VerificaAlugaCliente BEFORE insert
ON aluga
FOR EACH ROW
BEGIN
	call VerificaProcAlugaCliente(NEW.id_cliente_fk);
	
END$
DELIMITER ;