CREATE TABLE IF NOT EXISTS public.phone
(
    phone_id bigint NOT NULL DEFAULT nextval('phone_phone_id_seq'::regclass),
    phone_person bigint NOT NULL,
    phone_ddd character varying(3) COLLATE pg_catalog."default" NOT NULL,
    phone_number character varying(10) COLLATE pg_catalog."default" NOT NULL,
    created_at timestamp with time zone NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp with time zone,
    active record_status NOT NULL DEFAULT 1,
    CONSTRAINT phone_pkey PRIMARY KEY (phone_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.phone
    OWNER to postgres;