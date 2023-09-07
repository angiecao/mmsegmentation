_base_ = ['./san-vit-b16_coco-stuff164k-640x640.py']

model = dict(
    type='MultimodalEncoderDecoder',
    pretrained='pretrain/clip_vit_large_patch14_336.pth',
    encoder_resolution=0.7,
    image_encoder=dict(
        type='VisionTransformer',
        img_size=(336, 336),
        patch_size=14,
        patch_pad=0,
        embed_dims=1024,
        num_layers=18,
        num_heads=16,
        out_indices=(5, 11, 17),
    ),
    text_encoder=dict(
        type='CLIPTextEncoder',
        embed_dims=768,
        num_layers=12,
        num_heads=12,
        output_dims=768,
    ),
    decode_head=dict(
        type='SideAdapterCLIPHead',
        san_cfg=dict(clip_channels=1024, cfg_decoder=dict(num_heads=16)),
        maskgen_cfg=dict(
            num_layers=6,
            embed_dims=1024,
            num_heads=16,
            out_dims=768,
        )))

# By default, models are trained on 8 GPUs with 4 images per GPU
train_dataloader = dict(batch_size=4)
