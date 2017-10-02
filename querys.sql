
create table tb_customer_account(
	id_customer int primary key auto_increment,
    cpf_cnpj decimal(12,0) not null,
    nm_customer varchar(100) not null,
    is_active boolean not null,
    vl_total decimal(12,2) not null
);

select * from tb_customer_account;

alter table tb_customer_account auto_increment=1500;

alter table `testes`.`tb_customer_account` 
add unique index `cpf_cnpj_unico` (`cpf_cnpj` ASC);
