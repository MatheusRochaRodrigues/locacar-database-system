#-----------------------------------------------aluga----------------------------------------
DELIMITER $
CREATE PROCEDURE VerificaProcAlugaCarro (in auxID int)
BEGIN
	declare a int;
	select count(id) into a from carro where carro.id = auxID;
    if a = 0 then
		signal SQLSTATE '45000'
			set message_text = 'Esse Carro não Existe No Banco de Dados';
    end if;
	
END $
DELIMITER ;

#--------------------------------------------------cliente-------------------------------------------------
DELIMITER $
CREATE PROCEDURE VerificaProcAlugaCliente (in auxID int)
BEGIN
	declare a int;
	select count(id) into a from cliente where cliente.id = auxID;
    if a = 0 then
		signal SQLSTATE '45000'
			set message_text = 'Esse Cliente não Existe No Banco de Dados';
    end if;
	
END $
DELIMITER ;

#------------------------------------------------telefone----------------------------------------------
DELIMITER $
CREATE PROCEDURE VerificaProcTel (in auxID bigint,  out ex bool)
BEGIN
	declare a bigint;
	select count(telefone) into a from cliente where telefone = auxID;
    if a = 0 then
    set ex = true;
    else
    set ex = false;
    end if;
	
END $
DELIMITER ;

