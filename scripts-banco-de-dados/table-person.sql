CREATE TABLE IF NOT EXISTS public.person
(
    person_id bigint NOT NULL DEFAULT nextval('person_person_id_seq'::regclass),
    person_name character varying(20) COLLATE pg_catalog."default" NOT NULL,
    person_last_name character varying(20) COLLATE pg_catalog."default" NOT NULL,
    created_at timestamp with time zone NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp with time zone,
    active record_status NOT NULL DEFAULT 1,
    CONSTRAINT person_pkey PRIMARY KEY (person_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.person
    OWNER to postgres;