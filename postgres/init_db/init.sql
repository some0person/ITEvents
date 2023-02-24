create table news (
    id serial,
    date varchar not null,
    title varchar not null,
    link varchar not null,
    description varchar,
    date_updated varchar not null);

create unique index news_id_uindex
	on news (id);

alter table news
	add constraint news_pk
		primary key (id);
